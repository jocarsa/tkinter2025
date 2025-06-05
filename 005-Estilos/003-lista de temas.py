import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

style = ttk.Style()
# winnative,clam,alt,default,classic,vista,xpnative
style.theme_use("xpnative") 

style.configure("TLabel", foreground="blue", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12), padding=6)

# Crear y mostrar widgets con ttk
ttk.Label(ventana, text="Texto de prueba con estilo").pack(padx=20, pady=20)
ttk.Button(ventana, text="Aceptar", command=ventana.quit).pack()

# Ejecutar ventana
ventana.mainloop()
