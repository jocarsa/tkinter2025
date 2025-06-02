import tkinter as tk

def calculaIVA():
    precio = preciosiniva.get()
    precio = float(precio)
    iva = precio * 0.21
    resultado.config(text="IVA: "+str(iva)+"€")

ventana = tk.Tk()
ventana.title("Mi programa v0.1")
ventana.geometry("400x400")

tk.Label(ventana, text="Calculadora de IVA").pack(padx=10, pady=10)
tk.Label(ventana, text="v0.1").pack(padx=10, pady=5)

tk.Label(ventana, text="Introduce el precio sin IVA:").pack(padx=10, pady=5)
preciosiniva = tk.Entry(ventana)
preciosiniva.pack(padx=10, pady=5)

tk.Button(ventana, text="Calcular IVA",command=calculaIVA).pack(padx=10, pady=10)
resultado = tk.Label(ventana, text="El IVA es:")
resultado.pack(padx=10, pady=5)

ventana.mainloop()

