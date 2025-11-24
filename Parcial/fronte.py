import tkinter as tk
from tkinter import ttk, messagebox
import patra

ventana = tk.Tk()
ventana.title("JAHUCORP")
ventana.geometry("350x400")
ventana.config(bg="#565656")
tk.Label(ventana, text="SGI JAHU", font=("Calibri", 16, "bold"), fg="red", bg="#565656").pack(pady=10)
def agregar_categoria():
    win = tk.Toplevel(ventana)
    win.title("Agregar Categoría")
    win.geometry("250x120")
    tk.Label(win, text="Nombre Categoría:").pack(pady=5)
    entrada = tk.Entry(win)
    entrada.pack()
    def guardar():
        nombre = entrada.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese nombre de categoría.")
            return
        r = patra.agregar_categoria(nombre)
        messagebox.showinfo("Resultado", r)
        win.destroy()
    tk.Button(win, text="Guardar", command=guardar).pack(pady=10)
def agregar_producto():
    win = tk.Toplevel(ventana)
    win.title("Agregar Producto")
    win.geometry("300x300")
    campos = ["Código", "Nombre", "Categoría", "Cantidad", "Precio"]
    entradas = {}
    for c in campos:
        tk.Label(win, text=c).pack()
        e = tk.Entry(win)
        e.pack()
        entradas[c] = e
    def guardar():
        try:
            r = patra.agregarproducto(
                entradas["Código"].get(),
                entradas["Nombre"].get(),
                entradas["Categoría"].get(),
                entradas["Cantidad"].get(),
                entradas["Precio"].get()
            )
            messagebox.showinfo("Resultado", r)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    tk.Button(win, text="Guardar", command=guardar).pack(pady=10)
def ver_inventario():
    inv = patra.obtener_inv()
    win = tk.Toplevel(ventana)
    win.title("Inventario")
    win.geometry("500x300")
    cols = ("Código", "Nombre", "Categoría", "Cantidad", "Precio")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=90)
    tree.pack(expand=True, fill="both")
    for p in inv:
        tree.insert("", "end", values=p)
def crear_factura():
    win = tk.Toplevel(ventana)
    win.title("Crear Factura")
    win.geometry("350x400")
    tk.Label(win, text="Ingrese productos y cantidades:").pack(pady=5)
    frame = tk.Frame(win)
    frame.pack(pady=5, fill="both", expand=True)
    productos_frame = tk.Frame(frame)
    productos_frame.pack()
    tk.Label(productos_frame, text="Código").grid(row=0, column=0, padx=5)
    tk.Label(productos_frame, text="Cantidad").grid(row=0, column=1, padx=5)
    entradas = []
    def agregar_fila():
        e1 = tk.Entry(productos_frame, width=10)
        e2 = tk.Entry(productos_frame, width=10)
        row = len(entradas) + 1
        e1.grid(row=row, column=0, padx=5, pady=2)
        e2.grid(row=row, column=1, padx=5, pady=2)
        entradas.append((e1, e2))
    agregar_fila()
    def agregar_mas():
        agregar_fila()
    def guardar_factura():
        lista = []
        try:
            for e1, e2 in entradas:
                cod = e1.get().strip()
                cant = int(e2.get().strip())
                if cod and cant > 0:
                    lista.append((cod, cant))
            if not lista:
                messagebox.showwarning("Error", "Agrega al menos un producto con cantidad > 0.")
                return
            factos, total = patra.Cfactos(lista)
            msg = "Factura creada:\n"
            for f in factos:
                msg += f"{f[0]} x{f[1]} = ${f[3]:.2f}\n"
            msg += f"Total: ${total:.2f}"
            messagebox.showinfo("Factura", msg)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    tk.Button(win, text="Agregar más productos", command=agregar_mas).pack(pady=5)
    tk.Button(win, text="Crear Factura", command=guardar_factura).pack(pady=10)
def ver_facturas():
    factos = patra.obtfactoss()
    win = tk.Toplevel(ventana)
    win.title("Facturas")
    win.geometry("400x400")
    if not factos:
        tk.Label(win, text="No hay facturas.").pack(pady=10)
        return
    for idx, (detalles, total) in enumerate(factos):
        tk.Label(win, text=f"Factura {idx+1} - Total: ${total:.2f}", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
        for item in detalles:
            nombre, cantidad, precio, subtotal = item
            tk.Label(win, text=f"  {nombre} x{cantidad} = ${subtotal:.2f}").pack(anchor="w", padx=20)
        tk.Label(win, text="").pack()
tk.Button(ventana, text="Agregar Categoría", width=20, command=agregar_categoria).pack(pady=5)
tk.Button(ventana, text="Agregar Producto", width=20, command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="Ver Inventario", width=20, command=ver_inventario).pack(pady=5)
tk.Button(ventana, text="Crear Factura", width=20, command=crear_factura).pack(pady=5)
tk.Button(ventana, text="Ver Facturas", width=20, command=ver_facturas).pack(pady=5)

ventana.mainloop()
