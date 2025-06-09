import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Clientes")
root.geometry("700x500")
root.resizable(False, False)

# Frame para el formulario
formulario_frame = ttk.LabelFrame(root, text="Datos del Cliente", padding=10)
formulario_frame.pack(fill="x", padx=10, pady=10)

# Campos del formulario
ttk.Label(formulario_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
nombre_entry = ttk.Entry(formulario_frame, width=30)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(formulario_frame, text="Apellidos:").grid(row=1, column=0, sticky="w")
apellidos_entry = ttk.Entry(formulario_frame, width=30)
apellidos_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(formulario_frame, text="Email:").grid(row=2, column=0, sticky="w")
email_entry = ttk.Entry(formulario_frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(formulario_frame, text="Teléfono:").grid(row=3, column=0, sticky="w")
telefono_entry = ttk.Entry(formulario_frame, width=30)
telefono_entry.grid(row=3, column=1, padx=5, pady=5)

# Botones CRUD
botones_frame = ttk.Frame(root)
botones_frame.pack(fill="x", padx=10, pady=5)

ttk.Button(botones_frame, text="Crear").pack(side="left", padx=5)
ttk.Button(botones_frame, text="Leer").pack(side="left", padx=5)
ttk.Button(botones_frame, text="Actualizar").pack(side="left", padx=5)
ttk.Button(botones_frame, text="Eliminar").pack(side="left", padx=5)
ttk.Button(botones_frame, text="Limpiar").pack(side="left", padx=5)

# Tabla de clientes
tabla_frame = ttk.Frame(root)
tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

tabla = ttk.Treeview(tabla_frame, columns=("nombre", "apellidos", "email", "telefono"), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("apellidos", text="Apellidos")
tabla.heading("email", text="Email")
tabla.heading("telefono", text="Teléfono")

tabla.column("nombre", width=120)
tabla.column("apellidos", width=150)
tabla.column("email", width=180)
tabla.column("telefono", width=100)

tabla.pack(fill="both", expand=True)

# Ejecutar la aplicación
root.mainloop()
