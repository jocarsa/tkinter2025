import tkinter as tk
from tkinter import ttk
import json

# Leer el modelo de datos desde JSON
with open("modelo.json", "r", encoding="utf-8") as f:
    modelo = json.load(f)

# Obtener campos de clientes
campos = modelo["clientes"]

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")
root.geometry("800x500")
root.resizable(False, False)

# Frame del formulario
formulario_frame = ttk.LabelFrame(root, text="Datos del Cliente", padding=10)
formulario_frame.pack(fill="x", padx=10, pady=10)

# Diccionario para almacenar los Entry
entradas = {}

# Crear los campos dinámicamente
for i, campo in enumerate(campos):
    ttk.Label(formulario_frame, text=campo.capitalize() + ":").grid(row=i, column=0, sticky="w", padx=5, pady=5)
    entrada = ttk.Entry(formulario_frame, width=40)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas[campo] = entrada

# Botones CRUD
botones_frame = ttk.Frame(root)
botones_frame.pack(fill="x", padx=10, pady=5)

for texto in ["Crear", "Leer", "Actualizar", "Eliminar", "Limpiar"]:
    ttk.Button(botones_frame, text=texto).pack(side="left", padx=5)

# Tabla de clientes
tabla_frame = ttk.Frame(root)
tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

tabla = ttk.Treeview(tabla_frame, columns=campos, show="headings")

# Encabezados dinámicos
for campo in campos:
    tabla.heading(campo, text=campo.capitalize())
    tabla.column(campo, width=150)

tabla.pack(fill="both", expand=True)

# Ejecutar la aplicación
root.mainloop()
