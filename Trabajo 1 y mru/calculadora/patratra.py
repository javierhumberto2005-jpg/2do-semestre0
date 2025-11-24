expresion = ""
 #definimos
def AggNum(valor): #agregar numero
    global expresion
    expresion += str(valor)
    return expresion

def borrar(): #borrar
    global expresion
    expresion = ""
    return expresion

def calcular(): #Calcular
    global expresion
    try:
        resultado = str(eval(expresion))
        expresion = resultado
        return resultado
    except:
        expresion = ""
        return "Error de capa 8" #bueno
