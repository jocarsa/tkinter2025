import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Demo de Temas con ttk")
ventana.geometry("600x400")

# Lista de temas disponibles
style = ttk.Style()
temas = style.theme_names()
tema_actual = tk.StringVar(value=style.theme_use())

def cambiar_tema(event=None):
    style.theme_use(tema_actual.get())

# Aplicar un estilo base
style.configure("TLabel", font=("Segoe UI", 12), foreground="navy")
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TEntry", padding=4)
style.configure("TCombobox", padding=4)
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

# Selector de tema
ttk.Label(ventana, text="Selecciona un tema:").pack(pady=(10, 0))
combo_tema = ttk.Combobox(ventana, values=temas, textvariable=tema_actual, state="readonly")
combo_tema.pack()
combo_tema.bind("<<ComboboxSelected>>", cambiar_tema)

# Crear un Notebook con dos pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, pady=10, padx=10)

# Pestaña 1: formulario
frame1 = ttk.Frame(notebook)
ttk.Label(frame1, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(frame1).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame1, text="Correo:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(frame1).grid(row=1, column=1, padx=5, pady=5)

ttk.Button(frame1, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

# Pestaña 2: tabla
frame2 = ttk.Frame(notebook)
tree = ttk.Treeview(frame2, columns=("nombre", "edad"), show="headings")
tree.heading("nombre", text="Nombre")
tree.heading("edad", text="Edad")
tree.insert("", "end", values=("Juan", 30))
tree.insert("", "end", values=("Ana", 25))
tree.pack(fill="both", expand=True, padx=10, pady=10)

notebook.add(frame1, text="Formulario")
notebook.add(frame2, text="Datos")

# Ejecutar aplicación
ventana.mainloop()
