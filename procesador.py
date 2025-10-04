from conexion import conectar_rabbitmq
from datetime import datetime, timedelta

def calcular_fecha_parto(fecha_prenada: str) -> str:
    fecha = datetime.strptime(fecha_prenada, "%Y-%m-%d")
    fecha_parto = fecha + timedelta(days=120)
    return fecha_parto.strftime("%Y-%m-%d")

def verificar_vacuna(fecha_vacuna: str, dias_refuerzo: int) -> str:
    fecha = datetime.strptime(fecha_vacuna, "%Y-%m-%d")
    fecha_refuerzo = fecha + timedelta(days=dias_refuerzo)
    return fecha_refuerzo.strftime("%Y-%m-%d")

def procesar_evento(ch, method, properties, body):
    mensaje = body.decode()
    print(f"[Procesador] Evento recibido: {mensaje}")

    partes = mensaje.split("|")
    tipo = partes[0]
    resultado = "Evento no reconocido"

    if tipo == "prenada":
        _, cerda_id, fecha_prenada = partes
        fecha_parto = calcular_fecha_parto(fecha_prenada)
        resultado = f"La cerda {cerda_id} parirá alrededor del {fecha_parto}"

    elif tipo == "parto":
        _, cerda_id, cantidad, numero_parto = partes
        resultado = f"La cerda {cerda_id} tuvo {cantidad} lechones en el parto #{numero_parto}"

    elif tipo == "vacuna":
        _, cerda_id, fecha_vacuna, dias_refuerzo = partes
        fecha_refuerzo = verificar_vacuna(fecha_vacuna, int(dias_refuerzo))
        resultado = f"Vacuna aplicada a la cerda {cerda_id}, refuerzo recomendado el {fecha_refuerzo}"

    # Publicar el resultado
    conexion, canal = conectar_rabbitmq()
    canal.queue_declare(queue='resultados')
    canal.basic_publish(exchange='',
                        routing_key='resultados',
                        body=resultado)
    print(f"[Procesador] Resultado publicado: {resultado}")
    conexion.close()

def iniciar_procesador():
    conexion, canal = conectar_rabbitmq()
    canal.queue_declare(queue='eventos')
    canal.basic_consume(queue='eventos',
                        on_message_callback=procesar_evento,
                        auto_ack=True)
    print("[Procesador] Esperando eventos...")
    try:
        canal.start_consuming()
    except KeyboardInterrupt:
        conexion.close()

if __name__ == "__main__":
    iniciar_procesador()