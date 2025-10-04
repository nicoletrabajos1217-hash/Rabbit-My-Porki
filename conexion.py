import pika

def conectar_rabbitmq():
    """Establece conexión con RabbitMQ en localhost y devuelve conexión y canal."""
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexion.channel()
    return conexion, canal