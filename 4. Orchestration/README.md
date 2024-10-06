# Apache Airflow Exercises

## Table of Contents
- [Introduction (English)](#introduction-english)
- [Introducción (Español)](#introducción-español)
- [Installation / Instalación](#installation--instalación)
- [Usage / Uso](#usage--uso)
- [Stopping Airflow / Detener Airflow](#stopping-airflow--detener-airflow)

---

## Introduction (English)

This folder contains exercises to work with **Apache Airflow**, a platform to programmatically author, schedule, and monitor workflows. The exercises focus on building Directed Acyclic Graphs (DAGs) for data processing, orchestration, and ETL (Extract, Transform, Load) operations.

### What It Does

- **DAG Example 1**: A simple DAG containing only one task to showcase basic scheduling.
- **DAG Example 2**: A DAG with three tasks demonstrating dependencies between them.
- **DAG Example 3**: An ETL orchestration DAG with Python and Bash tasks, demonstrating Airflow's versatility in managing workflows.

### Key Tools:
- **Apache Airflow** for workflow orchestration.
- **Python** and **Bash** for task execution within DAGs.

---

## Introducción (Español)

Esta carpeta contiene ejercicios para trabajar con **Apache Airflow**, una plataforma para programar, planificar y monitorear flujos de trabajo. Los ejercicios se enfocan en la construcción de Grafos Acíclicos Dirigidos (DAGs) para el procesamiento de datos, orquestación y operaciones ETL (Extraer, Transformar, Cargar).

### Qué Hace

- **Ejemplo DAG 1**: Un DAG simple que contiene una sola tarea para mostrar la planificación básica.
- **Ejemplo DAG 2**: Un DAG con tres tareas que demuestran las dependencias entre ellas.
- **Ejemplo DAG 3**: Un DAG de orquestación ETL con tareas de Python y Bash, demostrando la versatilidad de Airflow en la gestión de flujos de trabajo.

### Herramientas Clave:
- **Apache Airflow** para la orquestación de flujos de trabajo.
- **Python** y **Bash** para la ejecución de tareas dentro de los DAGs.

---

## Installation / Instalación

### Using Terminal / Usando la Terminal

Apache Airflow requires a Python 3 environment. Starting with Airflow 2.7.0, Python versions 3.8, 3.9, 3.10, 3.11, and 3.12 are supported. Currently, only pip installation is officially supported.

Airflow necesita un entorno Python 3. A partir de la versión 2.7.0, Airflow es compatible con Python 3.8, 3.9, 3.10, 3.11 y 3.12. Actualmente, solo se soporta oficialmente la instalación vía pip.

#### Set Airflow Home (Optional) / Establecer el Directorio de Airflow (Opcional)

Airflow requires a home directory, and uses `~/airflow` by default. The environment variable `AIRFLOW_HOME` can be used to set a custom location.

Airflow requiere un directorio de trabajo, y usa `~/airflow` por defecto. La variable de entorno `AIRFLOW_HOME` puede usarse para definir una ubicación personalizada.

```bash
export AIRFLOW_HOME=~/airflow
```

#### Install Airflow / Instalar Airflow

Install Airflow using the constraints file, which is determined based on the version of Airflow and Python you are using.

Instala Airflow utilizando el archivo de restricciones, el cual se determina en función de la versión de Airflow y Python que estás utilizando.

```bash
AIRFLOW_VERSION=2.10.2
PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

#### Run Airflow Standalone / Ejecutar Airflow Standalone

The `airflow standalone` command initializes the database, creates a user, and starts all components.

El comando `airflow standalone` inicializa la base de datos, crea un usuario y arranca todos los componentes.

```bash
airflow standalone
```

#### Access the Airflow UI / Acceder a la Interfaz de Airflow

Visit `localhost:8080` in your browser and log in using the credentials provided in the terminal.

Visita `localhost:8080` en tu navegador e inicia sesión usando las credenciales mostradas en la terminal.

---

### Using Docker / Usando Docker

For Docker installation, follow these steps:

Para la instalación con Docker, sigue estos pasos:

1. Get **Visual Studio Code**.
2. Download the [Docker Compose file](https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml).
3. Open the downloaded `yaml` file in **Visual Studio Code**.
4. Create a new `.env` file and add the following lines:
```yaml
AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
AIRFLOW_UID=50000
```
5. Start the Airflow containers:

```bash
docker-compose up -d
```

6. Verify the running containers:

```bash
docker ps
```

7. Create an admin user with the following command:

```bash
docker-compose exec airflow-webserver airflow users create `
    --username "admin" `
    --firstname "Daniel" `
    --lastname "Godoy" `
    --role "Admin" `
    --email "daniel@example.com"
```

Alternatively, create another user via:

```bash
docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

Access the Airflow UI at [http://localhost:8080/](http://localhost:8080/).

Accede a la interfaz de Airflow en [http://localhost:8080/](http://localhost:8080/).

The Docker containers will keep running until explicitly stopped:

Los contenedores de Docker seguirán ejecutándose hasta que se detengan explícitamente:

```bash
docker-compose down
docker-compose stop
```

For more information, check the official Airflow documentation: [Airflow Installation Documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html).

Para más información, consulta la documentación oficial de Airflow: [Documentación de Instalación de Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start.html).

---

## Usage / Uso

The three examples in this folder demonstrate how to build DAGs incrementally.



1. **DAG Example 1**: Contains only one task. This is a basic introduction to DAG creation.
2. **DAG Example 2**: Contains three tasks, showcasing the ability to set task dependencies.
3. **DAG Example 3**: Simulates an ETL orchestration with both Python and Bash tasks, demonstrating the versatility of Airflow in data processing.

Los tres ejemplos en esta carpeta muestran cómo construir DAGs de manera incremental.
1. **Ejemplo DAG 1**: Contiene solo una tarea. Es una introducción básica a la creación de DAGs.

![Ejemplo1](https://github.com/adgodoyo/BigData/blob/main/4.%20Orchestration/Primer%20Ejemplo.png)

2. **Ejemplo DAG 2**: Contiene tres tareas, mostrando la capacidad de establecer dependencias.

![Ejemplo2]("Segundo Ejemplo.png")

3. **Ejemplo DAG 3**: Simula una orquestación ETL con tareas de Python y Bash, demostrando la versatilidad de Airflow en el procesamiento de datos.

![Ejemplo3]("Tercer Ejemplo.png")

---

## Stopping Airflow / Detener Airflow

### Stopping Standalone Airflow / Detener Airflow en modo Standalone
To stop Airflow, simply press `Ctrl+C` in the terminal where it's running.

Para detener Airflow, simplemente presiona `Ctrl+C` en la terminal donde se está ejecutando.

### Stopping Docker Containers / Detener los Contenedores de Docker
Use the following commands to stop the Docker containers:

Utiliza los siguientes comandos para detener los contenedores de Docker:

```bash
docker-compose down
docker-compose stop
```
