import tkinter as tk

ventana = tk.Tk()
menu = tk.Menu(ventana)
ventana.config(menu=menu)

menuarchivo = tk.Menu(menu, tearoff=0)
menuarchivo.add_command(label="Nuevo")
menuarchivo.add_command(label="Abrir")
menuarchivo.add_command(label="Guardar")
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Archivo", menu=menuarchivo)

ventana.mainloop()