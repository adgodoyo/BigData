from confluent_kafka import Consumer, KafkaException, KafkaError

c2 = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group_1',
    'auto.offset.reset': 'earliest'
})

c2.subscribe(['my_topic'])

try:
    while True:
        msg = c2.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        print(f"Consumer 2 received: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    c2.close()
