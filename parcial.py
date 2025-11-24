class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.velocidad = 0
    def acelerar(self, cant=10):
        self.velocidad += cant
    def frenar(self, cant=10):
        self.velocidad = max(0, self.velocidad - cant)
    def innformacion(self):
        return f"{self.nombre} | Velocidad: {self.velocidad} km/h"
class Carro(Vehiculo):
    def __init__(self, nombre, num_puertas):
        super().__init__(nombre)
        self.num_puertas = num_puertas
    def innformacion(self):
        return f"{self.nombre} | Puertas: {self.num_puertas} | Velocidad: {self.velocidad} km/h"
class Moto(Vehiculo):
    def __init__(self, nombre, cilindraje):
        super().__init__(nombre)
        self.cilindraje = cilindraje
    def innformacion(self):
        return f"{self.nombre} | {self.cilindraje}cc | Velocidad: {self.velocidad} km/h"
class Bicicleta(Vehiculo):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo
    def innformacion(self):
        return f"{self.nombre} | Tipo: {self.tipo} | Velocidad: {self.velocidad} km/h"
renault = Carro("Renault Logan", 5)
toyota = Carro("Toyota Prado", 5)
mazda = Carro("Mazda CX30", 5)
pulsar = Moto("Pulsar 200", 200)
victory = Moto("MRX 150", 150)
cicla1 = Bicicleta("Cicla GW", "Montaña")
cicla2 = Bicicleta("Cicla de Kick Buttowski", "BMX bajando el pico de la viuda")
vehiculos = [renault, toyota, mazda, pulsar, victory, cicla1, cicla2]
while True:
    print("\nVehiculos")
    for i, vehi in enumerate(vehiculos):
        print(f"{i+1}. {vehi.nombre}")
    opcion = int(input("Elija una opcion (0 para salir): "))
    if opcion == 0:
        print("Byes")
        break
    if 1 <= opcion <= len(vehiculos):
        vehi = vehiculos[opcion - 1]
        print(f"\n{vehi.nombre}")
        print("1. Acelerar")
        print("2. Frenar")
        hacer = int(input(" Que va a hacer?: "))
        if hacer == 1:
            cantidad = int(input("Cuantos km/h quiere acelerar?: "))
            vehi.acelerar(cantidad)
            print("RUN RUN!")
        elif hacer == 2:
            cantidad = int(input("Cuantos km/h quiere frenar?: "))
            vehi.frenar(cantidad)
            print("Freno, freno, Frenooo")
        else:
            print("Error capa 8, otra vez.")

        print(vehi.innformacion())
    else:
        print("No está disponible.")
