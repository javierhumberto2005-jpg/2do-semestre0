class Militar:
    def __init__(self, nombre, edad, rango):
        self.nombre = nombre
        self.edad = edad
        self.rango = rango
    def presentarse(self):
        return f"Mi w es {self.nombre}, {self.rango}, tengo {self.edad} años."
    def cumplir_orden(self):
        return f"{self.rango} {self.nombre} cumple la orden asignada."
class Soldado(Militar):
    def __init__(self, nombre, edad, rango, fusil):
        super().__init__(nombre, edad, rango)
        self.fusil = fusil
    def atacar(self):
        return f"{self.nombre} ataca usando su {self.fusil}."
class Piloto(Militar):
    def __init__(self, nombre, edad, rango, aeronave):
        super().__init__(nombre, edad, rango)
        self.aeronave = aeronave
    def volar(self):
        return f"{self.nombre} está volando un {self.aeronave}."
class Artillero(Militar):
    def __init__(self, nombre, edad, rango, calibre):
        super().__init__(nombre, edad, rango)
        self.calibre = calibre
    def disparar_artilleria(self):
        return f"{self.nombre} dispara ametralladora calibre {self.calibre}."
class Comandante(Militar):
    def __init__(self, nombre, edad, rango, unidad):
        super().__init__(nombre, edad, rango)
        self.unidad = unidad
    def dar_orden(self, orden):
        return f"El {self.rango} {self.nombre} ordena: {orden}"
class capitan(Militar):
    def __init__(self, nombre, edad, rango, unidad):
        super().__init__(nombre, edad, rango)
        self.unidad = unidad
    def dar_orden(self, orden):
        return f"La {self.rango} {self.nombre} ordena: {orden}"
if __name__ == "__main__":
    soldado = Soldado("Mont", 25, "Cabo", "Fusil Galil")
    piloto = Piloto("Llano", 30, "Teniente", "Avión Kfir")
    artillero = Artillero("Badillo", 28, "soldado", "12.7mm")
    comandante = Comandante("Moron", 45, "Comanndante", "Batallón 14")
    capitan = capitan("Martinez", 47, "Capitana", "Batallón 14")
    print(capitan.dar_orden("Atencion presentarse"))
    print(capitan.presentarse())
    print(soldado.presentarse())
    print(soldado.atacar())
    print(piloto.presentarse())
    print(piloto.volar())
    print(artillero.presentarse())
    print(artillero.disparar_artilleria())
    print(comandante.presentarse())
    print(comandante.dar_orden("Mantener la posición"))
    print(capitan.presentarse())
    print(" *SOLDADOS COREAN AJUA!* ")
    print(capitan.dar_orden(" ROMPAN FILAS "))