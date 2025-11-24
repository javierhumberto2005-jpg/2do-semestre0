class MIvida: 
    def __init__(self, nombre, color, edad, genero, altura, ocupacion):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.ocupacion = ocupacion
    def hablar(self):
        print(f"{self.nombre} dice: Hola! No soy negro, soy {self.color}, tambien soy un joven que le gusta los videojuegos, viajar, conocer pueblos, actualmente estudio ingenieria informatica en la unipaz y voy en el segundo semestre.")

jav = MIvida(f"Javier Llano","Marron","20 años","Hombre","1.74 cm","estudiante")


print(f"Mi nombre es: {jav.nombre}")
print(f"Tengo: {jav.edad}")
print(f"Soy: {jav.genero}")
print(f"Mido: {jav.altura}")
print(f"Soy: {jav.ocupacion}, de ing informatica")

jav.hablar()
