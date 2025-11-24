class Perro: 
    def __init__(self, nombre, color, genero):
        self.nombre = nombre
        self.color = color
        self.genero = genero
    def ladrar(self):
        print(f"{self.nombre} dice: wof soy de color {self.color}.")

perro1 = Perro(f"lolo","negro","macho")
perro2 = Perro(f"chanda","negro","macho")
perro3 = Perro(f"manolorrea","negro","macho")

print(f"el nombre del perro1 es: {perro1.nombre}")
print(f"el color del perro2 es: {perro2.color}")
print(f"el genero del perro3 es: {perro3.genero}")

perro1.ladrar()
perro2.ladrar()
perro3.ladrar()