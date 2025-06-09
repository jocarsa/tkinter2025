import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Configuración de la base de datos
DB_NOMBRE = "clientes.db"

# Función para obtener todas las tablas
def obtener_tablas():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    return [fila[0] for fila in cursor.fetchall()]

# Función para obtener columnas de una tabla (sin 'id')
def obtener_campos(tabla):
    cursor.execute(f"PRAGMA table_info({tabla})")
    columnas = cursor.fetchall()
    return [col[1] for col in columnas if col[1] != "id"]

# Inicialización
conn = sqlite3.connect(DB_NOMBRE)
cursor = conn.cursor()

root = tk.Tk()
root.title("Gestión General de la Empresa")
root.geometry("1000x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Diccionario para guardar datos de cada entidad
datos_entidades = {}

# Función para crear CRUD para una tabla
def crear_interfaz_crud(tabla):
    campos = obtener_campos(tabla)
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=tabla.capitalize())

    formulario = ttk.LabelFrame(frame, text="Formulario", padding=10)
    formulario.pack(fill="x", padx=10, pady=10)

    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(formulario, text=campo.capitalize()).grid(row=i, column=0, sticky="w", padx=5, pady=5)
        entrada = ttk.Entry(formulario, width=40)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo] = entrada

    # Tabla
    tabla_frame = ttk.Frame(frame)
    tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)
    tree = ttk.Treeview(tabla_frame, columns=campos, show="headings")
    for campo in campos:
        tree.heading(campo, text=campo.capitalize())
        tree.column(campo, width=150)
    tree.pack(fill="both", expand=True)

    # Funciones CRUD
    def crear():
        valores = [entradas[c].get() for c in campos]
        if any(v == "" for v in valores):
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
            return
        cursor.execute(
            f"INSERT INTO {tabla} ({', '.join(campos)}) VALUES ({', '.join(['?']*len(campos))})", valores
        )
        conn.commit()
        leer()
        limpiar()

    def leer():
        for fila in tree.get_children():
            tree.delete(fila)
        cursor.execute(f"SELECT id, {', '.join(campos)} FROM {tabla}")
        for fila in cursor.fetchall():
            tree.insert("", "end", iid=fila[0], values=fila[1:])

    def actualizar():
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selecciona", "Selecciona una fila.")
            return
        registro_id = seleccionado[0]
        valores = [entradas[c].get() for c in campos]
        cursor.execute(
            f"UPDATE {tabla} SET {', '.join(f'{c}=?' for c in campos)} WHERE id=?", (*valores, registro_id)
        )
        conn.commit()
        leer()
        limpiar()

    def eliminar():
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selecciona", "Selecciona una fila.")
            return
        registro_id = seleccionado[0]
        cursor.execute(f"DELETE FROM {tabla} WHERE id=?", (registro_id,))
        conn.commit()
        leer()
        limpiar()

    def limpiar():
        for entrada in entradas.values():
            entrada.delete(0, tk.END)

    def cargar_datos(event):
        seleccionado = tree.selection()
        if seleccionado:
            valores = tree.item(seleccionado[0], "values")
            for i, campo in enumerate(campos):
                entradas[campo].delete(0, tk.END)
                entradas[campo].insert(0, valores[i])

    tree.bind("<<TreeviewSelect>>", cargar_datos)

    # Botones
    botones = ttk.Frame(frame)
    botones.pack(fill="x", padx=10, pady=5)
    for texto, comando in [
        ("Crear", crear), ("Leer", leer), ("Actualizar", actualizar),
        ("Eliminar", eliminar), ("Limpiar", limpiar)
    ]:
        ttk.Button(botones, text=texto, command=comando).pack(side="left", padx=5)

    # Guardar referencias
    datos_entidades[tabla] = {
        "campos": campos,
        "entradas": entradas,
        "tree": tree,
        "leer": leer
    }

    leer()

# Crear interfaces para todas las tablas encontradas
for tabla in obtener_tablas():
    crear_interfaz_crud(tabla)

# Ejecutar
root.mainloop()
