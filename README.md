My Porki con RabbitMQ

Este proyecto utiliza RabbitMQ y Python para gestionar información de cerdas: preñez, partos y vacunas.
Consta de cuatro archivos principales:

conexion.py = establece la conexión a RabbitMQ.

procesador.py = procesa los eventos recibidos.

consumidor.py = muestra los resultados procesados.

productor.py = interfaz gráfica (Tkinter) para enviar eventos.

Requisitos

Python 3.8 o superior

RabbitMQ en ejecución en localhost (puerto 5672)

Instalar dependencias:

pip install pika

Ejecución

Abre tres terminales en la carpeta del proyecto y ejecuta en este orden:

Consumidor

python consumidor.py


Procesador

python procesador.py


Productor (interfaz gráfica)

python productor.py

Uso

En la interfaz gráfica puedes:

Registrar una cerda preñada y calcular fecha estimada de parto.

Registrar un parto indicando número de lechones y número de parto.

Registrar una vacuna y calcular la fecha de refuerzo.

Los resultados aparecerán en la terminal del consumidor.

