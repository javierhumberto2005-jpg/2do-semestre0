class Jefe:
    def __init__(self, nombre, edad, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
    def presentarse(self):
        return f"Me llamo {self.nombre}, {self.cargo}, tengo {self.edad} años."
    def cumplir_orden(self):
        return f"{self.cargo} {self.nombre} cumple la orden asignada."
class Empleado(Jefe):
    def __init__(self, nombre, edad, cargo, herramienta):
        super().__init__(nombre, edad, cargo)
        self.herramienta = herramienta
    def trabajar(self):
        return f"{self.nombre} Trabaja todo el dia en el sol con el {self.herramienta} y buen airecito."
if __name__ == "__main__":
    Empleado = Empleado("Jose", 25, "soy Agricultor", "el tractor")
    print(Empleado.presentarse())
    print(Empleado.trabajar())
    