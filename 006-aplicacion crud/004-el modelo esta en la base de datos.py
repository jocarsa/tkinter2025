import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Configuración
DB_NOMBRE = "clientes.db"
TABLA = "clientes"

# Conexión y cursor
conn = sqlite3.connect(DB_NOMBRE)
cursor = conn.cursor()

# Crear tabla si no existe (estructura fija de ejemplo)
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {TABLA} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellidos TEXT,
    email TEXT,
    telefono TEXT
)
""")
conn.commit()

# Obtener columnas desde SQLite (omitimos el campo 'id')
cursor.execute(f"PRAGMA table_info({TABLA})")
info_columnas = cursor.fetchall()
campos = [col[1] for col in info_columnas if col[1] != "id"]

# GUI
root = tk.Tk()
root.title(f"Gestión de {TABLA.capitalize()}")
root.geometry("800x500")

# Formulario dinámico
formulario_frame = ttk.LabelFrame(root, text="Datos", padding=10)
formulario_frame.pack(fill="x", padx=10, pady=10)

entradas = {}
for i, campo in enumerate(campos):
    ttk.Label(formulario_frame, text=campo.capitalize() + ":").grid(row=i, column=0, sticky="w", padx=5, pady=5)
    entrada = ttk.Entry(formulario_frame, width=40)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas[campo] = entrada

# CRUD
def crear():
    valores = [entradas[c].get() for c in campos]
    if any(v == "" for v in valores):
        messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
        return
    cursor.execute(
        f"INSERT INTO {TABLA} ({', '.join(campos)}) VALUES ({', '.join(['?']*len(campos))})", valores
    )
    conn.commit()
    leer()
    limpiar()

def leer():
    for fila in tabla.get_children():
        tabla.delete(fila)
    cursor.execute(f"SELECT id, {', '.join(campos)} FROM {TABLA}")
    for fila in cursor.fetchall():
        tabla.insert("", "end", iid=fila[0], values=fila[1:])

def actualizar():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Selecciona", "Selecciona una fila.")
        return
    cliente_id = seleccionado[0]
    valores = [entradas[c].get() for c in campos]
    cursor.execute(
        f"UPDATE {TABLA} SET {', '.join(f'{c}=?' for c in campos)} WHERE id=?", (*valores, cliente_id)
    )
    conn.commit()
    leer()
    limpiar()

def eliminar():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Selecciona", "Selecciona una fila.")
        return
    cliente_id = seleccionado[0]
    cursor.execute(f"DELETE FROM {TABLA} WHERE id=?", (cliente_id,))
    conn.commit()
    leer()
    limpiar()

def limpiar():
    for entrada in entradas.values():
        entrada.delete(0, tk.END)

def cargar_datos(event):
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado[0], "values")
        for i, campo in enumerate(campos):
            entradas[campo].delete(0, tk.END)
            entradas[campo].insert(0, valores[i])

# Botones
botones = ttk.Frame(root)
botones.pack(fill="x", padx=10, pady=5)

for texto, comando in [("Crear", crear), ("Leer", leer), ("Actualizar", actualizar), ("Eliminar", eliminar), ("Limpiar", limpiar)]:
    ttk.Button(botones, text=texto, command=comando).pack(side="left", padx=5)

# Tabla
tabla_frame = ttk.Frame(root)
tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

tabla = ttk.Treeview(tabla_frame, columns=campos, show="headings")
for campo in campos:
    tabla.heading(campo, text=campo.capitalize())
    tabla.column(campo, width=150)

tabla.bind("<<TreeviewSelect>>", cargar_datos)
tabla.pack(fill="both", expand=True)

# Carga inicial
leer()

# Mainloop
root.mainloop()
