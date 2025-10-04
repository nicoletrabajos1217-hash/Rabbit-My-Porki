from conexion import conectar_rabbitmq

def evento_procesado(ch, method, properties, body):
    """Recibe el resultado del procesamiento."""
    resultado = body.decode()
    print(f"[Consumidor] Resultado recibido: {resultado}")

def iniciar_consumidor():
    """Escucha resultados en la cola 'resultados'."""
    conexion, canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')
    canal.basic_consume(queue='resultados',
                        on_message_callback=evento_procesado,
                        auto_ack=True)
    print("[Consumidor] Esperando resultados...")
    try:
        canal.start_consuming()
    except KeyboardInterrupt:
        conexion.close()

if __name__ == "__main__":
    iniciar_consumidor()