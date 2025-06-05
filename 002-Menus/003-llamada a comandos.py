import tkinter as tk

def nuevo():
    print("Nuevo archivo creado")

def abrir():
    print("Archivo abierto")

def guardar():
    print("Archivo guardado")

ventana = tk.Tk()
menu = tk.Menu(ventana)
ventana.config(menu=menu)

menuarchivo = tk.Menu(menu, tearoff=0)
menuarchivo.add_command(label="Nuevo",command=nuevo)
menuarchivo.add_command(label="Abrir", command=abrir)   
menuarchivo.add_command(label="Guardar", command=guardar)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Archivo", menu=menuarchivo)

ventana.mainloop()