#definimos y los valores en float por si son decimales
def Cespacio(t, v): #calculo de espacio
    try:
        t = float(t)
        v = float(v)
        return round(t * v, 2)
    except ValueError:
        return "Error de valores vuelva a intentarlo"

def Cvelocidad(x, t): #calculo de velocidad
    try:
        x = float(x) 
        t = float(t)
        if t == 0:
            return "Error: división entre 0"
        return round(x / t, 2)
    except ValueError:
        return "Error de valores vuelva a intentarlo"

def Ctiempo(x, v): #calculo de tiempo
    try:
        x = float(x)
        v = float(v)
        if v == 0:
            return "Error: división entre 0"
        return round(x / v, 2)
    except ValueError:
        return "Error de valores vuelva a intentarlo"


