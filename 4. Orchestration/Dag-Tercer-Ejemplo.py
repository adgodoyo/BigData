from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
import pandas as pd
import requests
import os
from datetime import datetime, timedelta
import json

# Definir funciones para las tareas


def download_data(**kwargs):
    url = "https://jsonplaceholder.typicode.com/posts"  # API pública de ejemplo
    response = requests.get(url)
    data = response.json()
    output_path = "/tmp/data.json"
    
    # Guardar el JSON de manera correcta usando json.dump
    with open(output_path, "w") as f:
        json.dump(data, f)
    
    kwargs['ti'].xcom_push(key='data_path', value=output_path)
    print(f"Datos descargados en: {output_path}")

def process_data(**kwargs):
    data_path = kwargs['ti'].xcom_pull(key='data_path')
    df = pd.read_json(data_path)
    
    # Realizar alguna transformación de datos con pandas
    df['title_length'] = df['title'].apply(len)
    
    processed_path = "/tmp/processed_data.csv"
    df.to_csv(processed_path, index=False)
    print(f"Datos procesados y guardados en: {processed_path}")
    
    kwargs['ti'].xcom_push(key='processed_data_path', value=processed_path)

def cleanup_files():
    os.remove("/tmp/data.json")
    os.remove("/tmp/processed_data.csv")
    print("Archivos temporales eliminados.")

# Definir el DAG

default_args = {
    'owner': 'adgodoyo',
    'start_date': days_ago(1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='advanced_etl_pipeline',
    default_args=default_args,
    schedule_interval='*/2 * * * *',  # Se ejecuta cada 10 minutos
    catchup=False
) as dag:

    # Tarea 1: Descargar datos de una API
    download_task = PythonOperator(
        task_id='download_data',
        python_callable=download_data,
        provide_context=True
    )

    # Tarea 2: Procesar datos con pandas
    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        provide_context=True
    )

    # Tarea 3: Limpiar archivos temporales (BashOperator)
    cleanup_task = BashOperator(
        task_id='cleanup_files',
        bash_command='rm -f /tmp/data.json /tmp/processed_data.csv'
    )

    # Tarea 4: Notificar por correo electrónico si todo sale bien
    success_email = EmailOperator(
        task_id='send_success_email',
        to='adgodoyo@gmail.com',
        subject='ETL Pipeline Success',
        html_content='<p>El pipeline de ETL se completó con éxito.</p>'
    )

    # Tarea 5: Notificar por correo electrónico en caso de fallo
    failure_email = EmailOperator(
        task_id='send_failure_email',
        to='adgodoyo@gmail.com',
        subject='ETL Pipeline Failed',
        html_content='<p>El pipeline de ETL ha fallado. Revisa los logs.</p>',
        trigger_rule='one_failed'
    )

    # Definir el flujo de tareas
    download_task >> process_task >> cleanup_task >> success_email
    download_task >> failure_email
