import tkinter as tk

def borrar_marcos():
    for widget in ventana.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.pack_forget()

def clientes():
    borrar_marcos()
    marcoclientes.pack(fill=tk.BOTH, expand=True)

def productos():
    borrar_marcos()
    marcoproductos.pack(fill=tk.BOTH, expand=True)

def pedidos():
    borrar_marcos()
    marcopedidos.pack(fill=tk.BOTH, expand=True)

ventana = tk.Tk()
ventana.title("Gestión empresarial")
ventana.geometry("400x400")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

menuarchivo = tk.Menu(menu, tearoff=0)
menuarchivo.add_command(label="Clientes", command=clientes)
menuarchivo.add_command(label="Productos", command=productos)
menuarchivo.add_command(label="Pedidos", command=pedidos)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)

menu.add_cascade(label="Recursos", menu=menuarchivo)

# Marco Clientes
marcoclientes = tk.Frame(ventana)
tk.Label(marcoclientes, text="Aquí van los clientes").pack(padx=10, pady=10)
tk.Label(marcoclientes, text="Nombre de cliente").pack(padx=10, pady=5)
tk.Entry(marcoclientes).pack(padx=10, pady=5)
tk.Label(marcoclientes, text="Teléfono").pack(padx=10, pady=5)
tk.Entry(marcoclientes).pack(padx=10, pady=5)
tk.Label(marcoclientes, text="Correo electrónico").pack(padx=10, pady=5)
tk.Entry(marcoclientes).pack(padx=10, pady=5)
tk.Button(marcoclientes, text="Guardar").pack(padx=10, pady=10)

# Marco Productos
marcoproductos = tk.Frame(ventana)
tk.Label(marcoproductos, text="Aquí van los productos").pack(padx=10, pady=10)
tk.Label(marcoproductos, text="Nombre del producto").pack(padx=10, pady=5)
tk.Entry(marcoproductos).pack(padx=10, pady=5)
tk.Label(marcoproductos, text="Precio").pack(padx=10, pady=5)
tk.Entry(marcoproductos).pack(padx=10, pady=5)
tk.Label(marcoproductos, text="Stock disponible").pack(padx=10, pady=5)
tk.Entry(marcoproductos).pack(padx=10, pady=5)
tk.Button(marcoproductos, text="Guardar").pack(padx=10, pady=10)

# Marco Pedidos
marcopedidos = tk.Frame(ventana)
tk.Label(marcopedidos, text="Aquí van los pedidos").pack(padx=10, pady=10)
tk.Label(marcopedidos, text="ID del pedido").pack(padx=10, pady=5)
tk.Entry(marcopedidos).pack(padx=10, pady=5)
tk.Label(marcopedidos, text="Cliente").pack(padx=10, pady=5)
tk.Entry(marcopedidos).pack(padx=10, pady=5)
tk.Label(marcopedidos, text="Producto").pack(padx=10, pady=5)
tk.Entry(marcopedidos).pack(padx=10, pady=5)
tk.Label(marcopedidos, text="Cantidad").pack(padx=10, pady=5)
tk.Entry(marcopedidos).pack(padx=10, pady=5)
tk.Button(marcopedidos, text="Guardar").pack(padx=10, pady=10)

ventana.mainloop()
