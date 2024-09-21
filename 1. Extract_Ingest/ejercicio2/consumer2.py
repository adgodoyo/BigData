from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import pandas as pd
import os

def transform_data(data):
    df = pd.DataFrame(data)
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()
    return df

def save_to_csv(df, file_path):
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

def main():
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'taxi_rides_group2',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe(['taxi_rides'])

    csv_file_path = 'ejercicio2/taxi_rides.csv'

    try:
        while True:
            msg = consumer.poll(1.0)  # Esperar por un mensaje
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            data = json.loads(msg.value().decode('utf-8'))
            if isinstance(data, list) and all(isinstance(d, dict) for d in data):
                transformed_data = transform_data(data)
                save_to_csv(transformed_data, csv_file_path)
                consumer.commit()  # Confirmar manualmente el offset después de procesar el mensaje
                print("Data saved to CSV and offset committed")
            else:
                print("Received data is not in the expected format")
                print(data)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
