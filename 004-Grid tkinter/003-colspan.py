import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Grid Simple")

tk.Label(ventana, text="Primera celda").grid(row=0, column=0)


tk.Label(ventana, text="Segunda celda").grid(row=0, column=1)

tk.Label(ventana, text="Tercera celda y es larga").grid(row=1, column=0,columnspan=2)




ventana.mainloop()
