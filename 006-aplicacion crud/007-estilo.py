import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox

# Conectar a base de datos
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

def obtener_tablas():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    return [t[0] for t in cursor.fetchall()]

def obtener_columnas(tabla):
    cursor.execute(f"PRAGMA table_info({tabla})")
    return [col[1] for col in cursor.fetchall() if col[1] != "id"]

app = tb.Window(themename="flatly")  # o "darkly", "cosmo", "morph", etc.
app.title("Sistema de Gestión Empresarial")
app.geometry("1200x700")

# Cabecera
cabecera = tb.Frame(app, bootstyle="primary", padding=10)
cabecera.pack(fill="x")
tb.Label(cabecera, text="📊 Sistema de Gestión Empresarial", font=("Segoe UI", 16), bootstyle="inverse").pack(side="left")
tb.Label(cabecera, text="Usuario: admin", font=("Segoe UI", 10), bootstyle="inverse").pack(side="right")

# Contenedor principal
contenedor = tb.Frame(app)
contenedor.pack(fill="both", expand=True)

# Menú lateral izquierdo
menu = tb.Frame(contenedor, width=200, bootstyle="light")
menu.pack(side="left", fill="y")

# Zona principal derecha
zona = tb.Frame(contenedor, padding=10)
zona.pack(side="left", fill="both", expand=True)

# Almacena widgets activos por entidad
widgets_entidades = {}

def mostrar_entidad(tabla):
    for widget in zona.winfo_children():
        widget.destroy()

    campos = obtener_columnas(tabla)
    entradas = {}

    # Formulario
    form = tb.LabelFrame(zona, text=f"{tabla.capitalize()} - Formulario", padding=10)
    form.pack(fill="x", pady=10)

    for i, campo in enumerate(campos):
        tb.Label(form, text=campo.capitalize()).grid(row=i, column=0, sticky="w", padx=5, pady=5)
        entrada = tb.Entry(form, width=40)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo] = entrada

    # Tabla
    tabla_frame = tb.Frame(zona)
    tabla_frame.pack(fill="both", expand=True)
    tree = ttk.Treeview(tabla_frame, columns=campos, show="headings")
    for campo in campos:
        tree.heading(campo, text=campo.capitalize())
        tree.column(campo, width=150)
    tree.pack(fill="both", expand=True)

    def limpiar():
        for e in entradas.values():
            e.delete(0, "end")

    def cargar_datos(_):
        seleccionado = tree.selection()
        if seleccionado:
            valores = tree.item(seleccionado[0], "values")
            for i, campo in enumerate(campos):
                entradas[campo].delete(0, "end")
                entradas[campo].insert(0, valores[i])

    def crear():
        valores = [entradas[c].get() for c in campos]
        if any(v == "" for v in valores):
            messagebox.showwarning("Faltan datos", "Rellena todos los campos.")
            return
        cursor.execute(f"INSERT INTO {tabla} ({', '.join(campos)}) VALUES ({', '.join(['?']*len(campos))})", valores)
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
        sel = tree.selection()
        if not sel:
            messagebox.showinfo("Selecciona", "Elige un registro.")
            return
        id_ = sel[0]
        valores = [entradas[c].get() for c in campos]
        cursor.execute(f"UPDATE {tabla} SET {', '.join([f'{c}=?' for c in campos])} WHERE id=?", (*valores, id_))
        conn.commit()
        leer()

    def eliminar():
        sel = tree.selection()
        if not sel:
            messagebox.showinfo("Selecciona", "Elige un registro.")
            return
        id_ = sel[0]
        cursor.execute(f"DELETE FROM {tabla} WHERE id=?", (id_,))
        conn.commit()
        leer()
        limpiar()

    tree.bind("<<TreeviewSelect>>", cargar_datos)

    # Botones
    btns = tb.Frame(zona)
    btns.pack(fill="x", pady=10)
    for texto, cmd in [("Crear", crear), ("Leer", leer), ("Actualizar", actualizar), ("Eliminar", eliminar), ("Limpiar", limpiar)]:
        tb.Button(btns, text=texto, command=cmd, bootstyle="primary-outline").pack(side="left", padx=5)

    leer()

# Cargar menú lateral con tablas
for tabla in obtener_tablas():
    tb.Button(menu, text=tabla.capitalize(), width=25, bootstyle="secondary-link", command=lambda t=tabla: mostrar_entidad(t)).pack(pady=2, padx=5, anchor="w")

# Mostrar la primera por defecto
tablas = obtener_tablas()
if tablas:
    mostrar_entidad(tablas[0])

# Ejecutar
app.mainloop()
