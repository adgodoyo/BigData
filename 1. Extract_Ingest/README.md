# Kafka Exercises 



## Table of Contents 
- [Introduction (English)](#introduction-english) 
- [Introducción (Español)](#introducción-español) 
- [Installation / Instalación](#installation--instalación) 
- [Usage / Uso](#usage--uso) 
- [Stopping Kafka / Detener Kafka](#stopping-kafka--detener-kafka) 

--- 

## Introduction (English) 

This folder contains exercises to work with **Apache Kafka**, a distributed messaging system for real-time data streaming. The exercises focus on producing and consuming data in different formats and using Kafka as a central messaging hub. 

### What It Does 

- **Exercise 1**: Generates fictitious data from a producer and sends it to two different consumers. The first consumer processes the data in a simple manner, while the second consumer handles a more complex transformation. 
- **Exercise 2**: Reads data from a Parquet database and sends it to two different producers. One producer stores the data in CSV format, while the other saves it to a SQL database. 

### Key Tools: 
- **Confluent Kafka** and **kafka-python** for Kafka integration in Python. 
- **Pandas**, **PyArrow**, **FastParquet**, and **SQLAlchemy** for data processing and storage. 

---

## Introducción (Español) 

Esta carpeta contiene ejercicios para trabajar con **Apache Kafka**, un sistema de mensajería distribuido para el streaming de datos en tiempo real. Los ejercicios se centran en la producción y consumo de datos en diferentes formatos, utilizando Kafka como un centro de mensajería. 

### Qué Hace 

- **Ejercicio 1**: Genera datos ficticios desde un productor y los envía a dos consumidores diferentes. El primer consumidor procesa los datos de manera simple, mientras que el segundo consumidor realiza una transformación más compleja. 
- **Ejercicio 2**: Lee datos desde una base de datos en formato Parquet y los envía a dos productores diferentes. Un productor guarda los datos en formato CSV, mientras que el otro los almacena en una base de datos SQL. 

### Herramientas Clave: 
- **Confluent Kafka** y **kafka-python** para la integración de Kafka en Python. 
- **Pandas**, **PyArrow**, **FastParquet**, y **SQLAlchemy** para el procesamiento y almacenamiento de datos. 

---

## Installation / Instalación 

### Using Bash (Linux / Mac): 
1. Download and extract [Kafka](https://kafka.apache.org/downloads) (Binary downloads): 
   ```bash 
   tar -xzf kafka_2.13-3.7.1.tgz 
   cd kafka_2.13-3.7.1 
   ``` 
2. Start Zookeeper: 
   ```bash 
   bin/zookeeper-server-start.sh config/zookeeper.properties 
   ``` 
3. Start Kafka: 
   ```bash 
   bin/kafka-server-start.sh config/server.properties 
   ``` 

### Using Docker/ Usando Docker: 
1. Pull Kafka image: 
   ```bash 
   docker pull apache/kafka:3.7.1 
   ``` 
2. Run Kafka container: 
   ```bash 
   docker run -p 9092:9092 apache/kafka:3.7.1 
   ``` 
3. To start an existing container: 
   ```bash 
   docker start <container_name> 
   ``` 

## Virtual Enviroment - Crea un Entorno Virtual PowerShell (Windows): 
1. Create a virtual environment in the root folder: 
   ```bash 
   python -m venv mi_venv 
   ``` 
2. Activate the virtual environment: 
   ```bash 
   mi_venv\Scripts\activate 
   ``` 
3. Install Kafka and required libraries: 
   ```bash 
   pip install confluent_kafka kafka-python pandas pyarrow fastparquet sqlalchemy 
   ``` 

### Using Mac/Usando Mac: 
1. Activate the virtual environment: 
   ```bash 
   source nombre_del_entorno/bin/activate 
   ``` 
2. Install Kafka and required libraries: 
   ```bash 
   pip install confluent_kafka kafka-python pandas pyarrow fastparquet sqlalchemy 
   ``` 

---

## Usage / Uso 

1. Before running the exercises, make sure Zookeeper and Kafka are active (follow the installation instructions above). 
2. **Exercise 1**: Running producer and consumers: 
   ```bash 
   python ejercicio1/producer.py 
   python ejercicio1/consumer1.py 
   python ejercicio1/consumer2.py 
   ``` 
3. **Exercise 2**: Working with Parquet data: 
   ```bash 
   python ejercicio2/producer.py 
   python ejercicio2/consumer1.py 
   python ejercicio2/consumer2.py
   ``` 

### Additional Commands: 

To list Kafka topics: 
```bash 
bin/windows/kafka-topics.bat --list --zookeeper localhost:2181 
``` 

---

## Stopping Kafka / Detener Kafka 

1. To stop Zookeeper: 
   ```bash 
   bin/zookeeper-server-stop.sh 
   ``` 
2. To stop Kafka: 
   ```bash 
   bin/kafka-server-stop.sh 
   ``` 

---

### Troubleshooting / Solución de problemas: 

- If you encounter port issues, check for any processes using port 9092: 
   ```bash 
   netstat -aon | findstr 9092 
   ``` 
- Enable Telnet to troubleshoot ports: 
   ```bash 
   dism /online /Enable-Feature /FeatureName:TelnetClient 
   telnet localhost 9092 
   ``` 
