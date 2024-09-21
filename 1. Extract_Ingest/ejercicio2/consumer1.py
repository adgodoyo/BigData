from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import pandas as pd
from sqlalchemy import create_engine

def transform_data(data):
    df = pd.DataFrame(data)
    # Realizar transformaciones necesarias, por ejemplo:
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()
    return df

def load_to_db(df, db_engine):
    df.to_sql('taxi_rides', db_engine, if_exists='append', index=False)

def main():
    consumer_conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'taxi_rides_group1',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe(['taxi_rides'])
    db_engine = create_engine('sqlite:///ejercicio2/taxi_rides.db')

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
            # Verificar si data es una lista de diccionarios
            if isinstance(data, list) and all(isinstance(d, dict) for d in data):
                transformed_data = transform_data(data)
                load_to_db(transformed_data, db_engine)
                consumer.commit()
                print("Data loaded to DB")
            else:
                print("Received data is not in the expected format")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
