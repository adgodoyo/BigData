from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Definir la función que se ejecutará
def my_task():
    print("¡Hola desde mi primer DAG en Airflow!")

# Definir el DAG
default_args = {
    'owner': 'adgodoyo',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
}

with DAG(
    dag_id='my_first_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    # Definir la tarea
    task = PythonOperator(
        task_id='my_first_task',
        python_callable=my_task,
    )

    task
