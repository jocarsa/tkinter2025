import tkinter as tk

def clientes():
    for widget in ventana.winfo_children():
        widget.pack_forget()
    marcoclientes.pack(fill=tk.BOTH, expand=True)
def productos():
    for widget in ventana.winfo_children():
        widget.pack_forget()
    marcoproductos.pack(fill=tk.BOTH, expand=True)
def pedidos():
    for widget in ventana.winfo_children():
        widget.pack_forget()
    marcopedidos.pack(fill=tk.BOTH, expand=True)

ventana = tk.Tk()
menu = tk.Menu(ventana)
ventana.config(menu=menu)

menuarchivo = tk.Menu(menu, tearoff=0)
menuarchivo.add_command(label="clientes",command=clientes)
menuarchivo.add_command(label="productos",command=productos)   
menuarchivo.add_command(label="pedidos",command=pedidos)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Recursos", menu=menuarchivo)

marcoclientes = tk.Frame(ventana)
tk.Label(marcoclientes, text="Aquí van los clientes").pack(padx=10, pady=10)

marcoproductos = tk.Frame(ventana)
tk.Label(marcoproductos, text="Aquí van los productos").pack(padx=10, pady=10)

marcopedidos = tk.Frame(ventana)
tk.Label(marcopedidos, text="Aquí van los pedidos").pack(padx=10, pady=10)


ventana.mainloop()