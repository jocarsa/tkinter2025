import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import json
import os

# Leer modelo desde JSON
with open("modelo.json", "r", encoding="utf-8") as f:
    modelo = json.load(f)

entidad = "clientes"
campos = modelo[entidad]

# Conexión a SQLite
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Crear tabla si no existe
columnas_sql = ", ".join([f"{campo} TEXT" for campo in campos])
cursor.execute(f"CREATE TABLE IF NOT EXISTS {entidad} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columnas_sql})")
conn.commit()

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")
root.geometry("800x500")

# Frame del formulario
formulario_frame = ttk.LabelFrame(root, text="Datos del Cliente", padding=10)
formulario_frame.pack(fill="x", padx=10, pady=10)

entradas = {}
for i, campo in enumerate(campos):
    ttk.Label(formulario_frame, text=campo.capitalize() + ":").grid(row=i, column=0, sticky="w", padx=5, pady=5)
    entrada = ttk.Entry(formulario_frame, width=40)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas[campo] = entrada

# Funciones CRUD
def crear_cliente():
    valores = [entradas[c].get() for c in campos]
    if any(v == "" for v in valores):
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return
    cursor.execute(f"INSERT INTO {entidad} ({', '.join(campos)}) VALUES ({', '.join('?' for _ in campos)})", valores)
    conn.commit()
    leer_clientes()
    limpiar_campos()

def leer_clientes():
    for fila in tabla.get_children():
        tabla.delete(fila)
    cursor.execute(f"SELECT id, {', '.join(campos)} FROM {entidad}")
    for fila in cursor.fetchall():
        tabla.insert("", "end", iid=fila[0], values=fila[1:])

def actualizar_cliente():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Sin selección", "Selecciona un cliente para actualizar.")
        return
    cliente_id = seleccionado[0]
    valores = [entradas[c].get() for c in campos]
    cursor.execute(f"UPDATE {entidad} SET {', '.join([f'{c}=?' for c in campos])} WHERE id=?", (*valores, cliente_id))
    conn.commit()
    leer_clientes()
    limpiar_campos()

def eliminar_cliente():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Sin selección", "Selecciona un cliente para eliminar.")
        return
    cliente_id = seleccionado[0]
    cursor.execute(f"DELETE FROM {entidad} WHERE id=?", (cliente_id,))
    conn.commit()
    leer_clientes()
    limpiar_campos()

def limpiar_campos():
    for entrada in entradas.values():
        entrada.delete(0, tk.END)

def cargar_datos_formulario(event):
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado[0], "values")
        for i, campo in enumerate(campos):
            entradas[campo].delete(0, tk.END)
            entradas[campo].insert(0, valores[i])

# Botones
botones_frame = ttk.Frame(root)
botones_frame.pack(fill="x", padx=10, pady=5)

ttk.Button(botones_frame, text="Crear", command=crear_cliente).pack(side="left", padx=5)
ttk.Button(botones_frame, text="Leer", command=leer_clientes).pack(side="left", padx=5)
ttk.Button(botones_frame, text="Actualizar", command=actualizar_cliente).pack(side="left", padx=5)
ttk.Button(botones_frame, text="Eliminar", command=eliminar_cliente).pack(side="left", padx=5)
ttk.Button(botones_frame, text="Limpiar", command=limpiar_campos).pack(side="left", padx=5)

# Tabla
tabla_frame = ttk.Frame(root)
tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

tabla = ttk.Treeview(tabla_frame, columns=campos, show="headings")
for campo in campos:
    tabla.heading(campo, text=campo.capitalize())
    tabla.column(campo, width=150)
tabla.bind("<<TreeviewSelect>>", cargar_datos_formulario)
tabla.pack(fill="both", expand=True)

# Cargar datos al inicio
leer_clientes()

# Ejecutar
root.mainloop()
