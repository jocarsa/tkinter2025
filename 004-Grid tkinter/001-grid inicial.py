import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Grid Simple")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Entry(ventana).grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0)
tk.Entry(ventana).grid(row=1, column=1)

tk.Button(ventana, text="Enviar").grid(row=2, column=0, columnspan=2)

ventana.mainloop()
