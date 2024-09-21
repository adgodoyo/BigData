from confluent_kafka import Consumer, KafkaException, KafkaError

c1 = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group_2',
    'auto.offset.reset': 'earliest'
})

c1.subscribe(['my_topic'])

try:
    while True:
        msg = c1.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f"Consumer 1 received: {msg.value().decode('utf-8')}")
        c1.commit() # confirmación de que el mensaje fue consumido
except KeyboardInterrupt:
    pass
finally:
    c1.close()
