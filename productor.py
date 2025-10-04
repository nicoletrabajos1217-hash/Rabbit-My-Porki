import tkinter as tk
from tkinter import ttk, messagebox
from conexion import conectar_rabbitmq

def publicar_evento(mensaje: str):
    conexion, canal = conectar_rabbitmq()
    canal.queue_declare(queue='eventos')
    canal.basic_publish(exchange='',
                        routing_key='eventos',
                        body=mensaje)
    conexion.close()
    messagebox.showinfo("Éxito", f"Evento enviado:\n{mensaje}")

# ----------- Funciones ----------
def enviar_prenada():
    cerda_id = entry_id.get()
    fecha = entry_fecha.get()
    if not cerda_id or not fecha:
        messagebox.showwarning("Error", "Completa ID y Fecha")
        return
    mensaje = f"prenada|{cerda_id}|{fecha}"
    publicar_evento(mensaje)

def enviar_parto():
    cerda_id = entry_id.get()
    cantidad = entry_cantidad.get()
    numero = entry_numero_parto.get()
    if not cerda_id or not cantidad or not numero:
        messagebox.showwarning("Error", "Completa todos los campos de parto")
        return
    mensaje = f"parto|{cerda_id}|{cantidad}|{numero}"
    publicar_evento(mensaje)

def enviar_vacuna():
    cerda_id = entry_id.get()
    fecha = entry_fecha.get()
    dias = entry_refuerzo.get()
    if not cerda_id or not fecha or not dias:
        messagebox.showwarning("Error", "Completa todos los campos de vacuna")
        return
    mensaje = f"vacuna|{cerda_id}|{fecha}|{dias}"
    publicar_evento(mensaje)

# ----------- Interfaz gráfica ----------
root = tk.Tk()
root.title("Gestión de Cerdas - Productor")
root.geometry("400x400")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="ID Cerda:").pack(anchor="w")
entry_id = ttk.Entry(frame)
entry_id.pack(fill="x")

ttk.Label(frame, text="Fecha (YYYY-MM-DD):").pack(anchor="w")
entry_fecha = ttk.Entry(frame)
entry_fecha.pack(fill="x")

ttk.Label(frame, text="Cantidad de lechones (parto):").pack(anchor="w")
entry_cantidad = ttk.Entry(frame)
entry_cantidad.pack(fill="x")

ttk.Label(frame, text="Número de parto:").pack(anchor="w")
entry_numero_parto = ttk.Entry(frame)
entry_numero_parto.pack(fill="x")

ttk.Label(frame, text="Días refuerzo (vacuna):").pack(anchor="w")
entry_refuerzo = ttk.Entry(frame)
entry_refuerzo.pack(fill="x")

ttk.Button(root, text="Registrar Prenada", command=enviar_prenada).pack(pady=5)
ttk.Button(root, text="Registrar Parto", command=enviar_parto).pack(pady=5)
ttk.Button(root, text="Registrar Vacuna", command=enviar_vacuna).pack(pady=5)

root.mainloop()