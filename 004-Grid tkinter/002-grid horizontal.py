import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Grid Simple")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Entry(ventana).grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=0, column=2)
tk.Entry(ventana).grid(row=0, column=3)

tk.Button(ventana, text="Enviar").grid(row=0, column=4)

ventana.mainloop()
