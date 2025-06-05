import tkinter as tk


ventana = tk.Tk()
menu = tk.Menu(ventana)
ventana.config(menu=menu)

menuarchivo = tk.Menu(menu, tearoff=0)
menuarchivo.add_command(label="clientes")
menuarchivo.add_command(label="productos")   
menuarchivo.add_command(label="pedidos")
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Recursos", menu=menuarchivo)

ventana.mainloop()