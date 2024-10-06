from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Definir funciones para las tareas
def extract():
    print("Extrayendo datos...")
    # Aquí podrías conectar a una base de datos y extraer datos
    return "datos_extraidos"

def transform(data):
    print(f"Transformando datos: {data}")
    # Aquí podrías procesar los datos, por ejemplo, limpiarlos o convertir formatos
    return data.upper()

def load(data):
    print(f"Cargando datos: {data}")
    # Aquí podrías cargar los datos en un data warehouse o en otro sistema
    print("Datos cargados con éxito")

# Definir el DAG
default_args = {
    'owner': 'adgodoyo',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='0.etl_pipeline',
    default_args=default_args,
    schedule_interval='*/1 * * * *',  # Se ejecuta cada 1 minuto
    catchup=False
) as dag:

    # Definir las tareas
    task_extract = PythonOperator(
        task_id='extract_task',
        python_callable=extract,
    )

    task_transform = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
        op_args=['{{ ti.xcom_pull(task_ids="extract_task") }}'], #TaskInstance
    )

    task_load = PythonOperator(
        task_id='load_task',
        python_callable=load,
        op_args=['{{ ti.xcom_pull(task_ids="transform_task") }}'],
    )

    # Definir el orden de las tareas
    task_extract >> task_transform >> task_load
