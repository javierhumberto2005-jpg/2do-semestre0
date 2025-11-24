import tkinter as tk
from back import Cespacio, Ctiempo, Cvelocidad

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora MRU")
ventana.geometry("400x400")
ventana.resizable(False, False)

#NI IDEA, lo vi en youtube
x_var = tk.StringVar()
t_var = tk.StringVar()
v_var = tk.StringVar()
resultado_var = tk.StringVar()
formula_var = tk.StringVar()

#definimos 
def calcular_x(): #calcular distancia
    resultado = Cespacio(t_var.get(), v_var.get())
    resultado_var.set(f"Espacio (x) = {resultado}")
    formula_var.set("x = t * v")

def calcular_t(): #calcular tiempo
    resultado = Ctiempo(x_var.get(), v_var.get())
    resultado_var.set(f"Tiempo (t) = {resultado}")
    formula_var.set("t = x / v")

def calcular_v(): #calcular velocidad
    resultado = Cvelocidad(x_var.get(), t_var.get())
    resultado_var.set(f"Velocidad (v) = {resultado}")
    formula_var.set("v = x / t")

def borrar(): #borrar datos
    x_var.set("")
    t_var.set("")
    v_var.set("")
    resultado_var.set("")
    formula_var.set("")
#titulo
tk.Label(ventana, text="JAHU MRU", font=("Calibri", 16, "bold")).pack(pady=10)
frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=10)

# Entradas
tk.Label(frame_inputs, text="Espacio (x): ").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame_inputs, textvariable=x_var).grid(row=0, column=1)

tk.Label(frame_inputs, text="Tiempo (t): ").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame_inputs, textvariable=t_var).grid(row=1, column=1)

tk.Label(frame_inputs, text="Velocidad (v): ").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(frame_inputs, textvariable=v_var).grid(row=2, column=1)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="Calcular X", command=calcular_x, width=10, bg="#ffff66", fg="black").grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Calcular V", command=calcular_v, width=10, bg="#ffff66", fg="black").grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Calcular T", command=calcular_t, width=10, bg="#f0f075", fg="black").grid(row=0, column=1, padx=5)


tk.Button(ventana, text="BORRAR", command=borrar, bg="#000099", fg="white", width=15).pack(pady=10)

# Resultados
tk.Label(ventana, text="Fórmula:", font=("Calibri", 10, "bold")).pack()
tk.Label(ventana, textvariable=formula_var, font=("Arial", 10)).pack()

tk.Label(ventana, text="Resultado:", font=("Calibri", 10, "bold")).pack()
tk.Label(ventana, textvariable=resultado_var, font=("Calibri", 12), fg="red").pack()
ventana.mainloop()
