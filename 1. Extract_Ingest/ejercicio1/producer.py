from confluent_kafka import Producer
import time # se puede utilizar para realizar pausas

def acked(err, msg): #Esta función es llamada cuando Kafka reconoce (acknowledges) que ha recibido el mensaje:
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

p = Producer({'bootstrap.servers': 'localhost:9092'}) #Vamos a crear una instancia para crear un productor
# 'bootstrap.servers' es un parámetro necesario que especifica el broker de Kafka al que se conectará el productor

for i in range(10):
    message = f"Message {i}"
    p.produce('my_topic', value=message, callback=acked)
    p.poll(1)

p.flush()


'''
Métodos de la clase Produce:

1. Método produce
El método produce se usa para enviar mensajes a un topic en Kafka. Aquí está la sintaxis general 
y los parámetros más importantes que se pueden usar con produce:

p.produce(topic, value=None, key=None, partition=None, callback=None, on_delivery=None, timestamp=None, headers=None)

**Parámetros del Método produce

topic (requerido):
Especifica el nombre del topic al que se enviará el mensaje.
Ejemplo: 'my_topic'

value (opcional):
El valor del mensaje que se enviará. Puede ser de tipo str, bytes, o None.
Ejemplo: value="Message 1"

key (opcional):
La clave del mensaje. Es opcional y puede ser de tipo str, bytes, o None. Las claves son útiles para garantizar que los mensajes con la misma clave siempre se envíen a la misma partición.
Ejemplo: key="key1"

partition (opcional):
El número de partición a la que se enviará el mensaje. Si no se especifica, Kafka usará un particionador para determinar la partición.
Ejemplo: partition=0

callback (opcional):
Una función de callback que se llamará una vez que el mensaje se haya enviado (o si ocurre un error).
Es muy importante para gestionar la confirmación de entrega de mensajes. 
Este parámetro permite especificar una función que será llamada cuando Kafka haya procesado el mensaje, ya sea entregándolo exitosamente o fallando en el intento. 
Esta función debe aceptar dos argumentos: err y msg.
err es un objeto que contiene información sobre el posible error
msd es el mensaje que se intentó enviar y tiene como atributos  el valor del mensaje, la clave, el offset, el topic, y la partición.
Ejemplo: callback=acked

timestamp (opcional):
Un timestamp para el mensaje. Puede ser None (el valor predeterminado), 0 (ningún timestamp), o un timestamp específico en milisegundos desde la época Unix (Unix epoch).
Ejemplo: timestamp=1622213447123

headers (opcional):
Un diccionario de encabezados de mensajes. Los encabezados permiten adjuntar metadatos adicionales al mensaje.
Ejemplo: headers={"header_key": "header_value"}




2.Función del Método poll
El método poll en el contexto de un productor de Kafka tiene dos roles principales:
1. Procesamiento de Callbacks: poll permite al productor procesar eventos y callbacks asociados a la entrega de mensajes. 
Cuando envías un mensaje con produce, especificas un callback (acked en el ejemplo anterior) que se llamará cuando Kafka reconozca la recepción del mensaje. 
poll es responsable de invocar estos callbacks.

Gestión Interna del Cliente: Kafka utiliza poll para llevar a cabo tareas internas necesarias para el buen funcionamiento del cliente, 
como la gestión de conexiones de red y el manejo de tiempos de espera.

Por Qué poll es Necesario
Eventos Asíncronos: La producción de mensajes en Kafka es asíncrona. Esto significa que cuando llamas a produce, el mensaje se pone en cola y la función regresa inmediatamente. La entrega real del mensaje ocurre en segundo plano, y poll asegura que se procesen estos eventos y se llamen los callbacks apropiados.
Gestión de Recursos: poll maneja tareas internas como la gestión de conexiones de red y tiempos de espera, asegurando que el cliente Kafka opere eficientemente.
Callback Handling: Sin poll, los callbacks no se invocarían, y no podrías manejar la confirmación de entrega de mensajes, errores, o cualquier otra lógica de post-envío.


'''

