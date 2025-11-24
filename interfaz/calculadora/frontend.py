import tkinter as tk
from patratra import AggNum, borrar, calcular

#ventana 
ventana = tk.Tk()
ventana.title("SENA")
tk.Label(ventana, text="JAHUCALCSENA", font=("Calibri", 16, "bold")).pack(pady=1)
ventana.geometry("310x470")
ventana.config(bg="#565656")
ventana.resizable(False, False)

label_resultado = tk.Label(ventana, text="", anchor="e", font=("Calibri", 24), bg="#ffffff", fg="#000000", relief="sunken", padx=3)
label_resultado.pack(pady=3, fill="x", padx=3)

#definimos
def cBoton(valor): #al dar click en botones
    nuevo_texto = AggNum(valor)
    label_resultado.config(text=nuevo_texto)

def cBorrar(): #al dar click en borrar
    label_resultado.config(text=borrar())

def cIgual(): #al dar click en igual
    label_resultado.config(text=calcular())

#marco de los botones
frame_botones = tk.Frame(ventana, bg="#565656")
frame_botones.pack()

#teclado
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 4, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 3, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 2, 3),
    ('0', 4, 0), ('Borrar', 4, 1), ('=', 4, 2), ('/', 1, 3),
]

#botones
for (texto, fila, columna) in botones:
    if texto == "Borrar":
        boton = tk.Button(frame_botones, text=texto, width=5, height=3, font=("Calibri", 14), bg="#ad8a1f", fg="red",
                          command=cBorrar)
    elif texto == "=":
        boton = tk.Button(frame_botones, text=texto, width=5, height=3, font=("Calibri", 14), bg="#666666", fg="red",
                          command=cIgual)
    else:
        boton = tk.Button(frame_botones, text=texto, width=5, height=3, font=("Calibri", 14), bg="#333c87", fg="white",
                          command=lambda valor=texto: cBoton(valor))
    
    boton.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()
