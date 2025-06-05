import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Crear ventana principal
ventana = ttk.Window(title="Demo de Temas con ttkbootstrap", themename="superhero", size=(700, 450))

# Obtener temas disponibles
temas = ventana.style.theme_names()
tema_actual = ttk.StringVar(value=ventana.style.theme.name)

# Función para cambiar tema
def cambiar_tema(event=None):
    ventana.style.theme_use(tema_actual.get())

# Selector de tema
ttk.Label(ventana, text="Selecciona un tema:", bootstyle="info").pack(pady=(10, 0))
combo_tema = ttk.Combobox(ventana, values=temas, textvariable=tema_actual, state="readonly", bootstyle="warning")
combo_tema.pack()
combo_tema.bind("<<ComboboxSelected>>", cambiar_tema)

# Notebook con pestañas
notebook = ttk.Notebook(ventana, bootstyle="primary")
notebook.pack(fill="both", expand=True, pady=10, padx=10)

# Pestaña 1: formulario
frame1 = ttk.Frame(notebook)
ttk.Label(frame1, text="Nombre:", bootstyle="info").grid(row=0, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(frame1, width=30, bootstyle="success").grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame1, text="Correo:", bootstyle="info").grid(row=1, column=0, sticky="e", padx=5, pady=5)
ttk.Entry(frame1, width=30, bootstyle="success").grid(row=1, column=1, padx=5, pady=5)

ttk.Button(frame1, text="Enviar", bootstyle="success").grid(row=2, column=0, columnspan=2, pady=10)

# Pestaña 2: tabla
frame2 = ttk.Frame(notebook)
tree = ttk.Treeview(frame2, columns=("nombre", "edad"), show="headings", bootstyle="info")
tree.heading("nombre", text="Nombre")
tree.heading("edad", text="Edad")
tree.insert("", "end", values=("Juan", 30))
tree.insert("", "end", values=("Ana", 25))
tree.pack(fill="both", expand=True, padx=10, pady=10)

notebook.add(frame1, text="Formulario")
notebook.add(frame2, text="Datos")

# Ejecutar aplicación
ventana.mainloop()
