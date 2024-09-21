from confluent_kafka import Producer
import pandas as pd
import json
import time

def read_parquet_in_chunks(file_path, chunksize=1000):
    parquet_file = pd.read_parquet(file_path, engine='pyarrow', columns=None)
    for start in range(0, len(parquet_file), chunksize):
        yield parquet_file[start:start + chunksize]

def send_to_kafka(producer, topic, data):
    producer.produce(topic, value=json.dumps(data, default=str).encode('utf-8'))
    producer.flush()  # Asegurar que el mensaje se envíe
    time.sleep(2)  # Simular un flujo de datos en tiempo real

def main():
    producer_conf = {
        'bootstrap.servers': 'localhost:9092'
    }
    producer = Producer(**producer_conf)
    
    parquet_chunks = read_parquet_in_chunks('ejercicio2/yellow_tripdata_2024-01.parquet')

    for chunk in parquet_chunks:
        data = chunk.to_dict(orient='records')
        send_to_kafka(producer, 'taxi_rides', data)
        print(data[:1])
        print("Chunk sent to Kafka")
    producer.flush()  # Asegurarse de que todos los mensajes se envíen

if __name__ == "__main__":
    main()
