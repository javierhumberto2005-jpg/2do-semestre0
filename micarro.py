class Carro: 
    def __init__(self, nombre, color, modelo, altura, tipo, ocupantes):
        self.nombre = nombre
        self.color = color
        self.modelo = modelo
        self.altura = altura
        self.tipo = tipo
        self.ocupantes = ocupantes
    def Acelerar(self):
        print(f"{self.nombre} Ruge: Run! Soy un vehiculo destinado al transporte de mi dueño, soy un modelo un poco nuevo, tengo poco kilometraje, apenas 43 mil kms.")

car = Carro(f"Renault Logan","Beige Dune","2021","libre al suelo de 18 cm","sedan", "max 5 pasajeros")


print(f"El vehiculo es un: {car.nombre}")
print(f"Color: {car.color}")
print(f"Modelo: {car.modelo}")
print(f"Altura al suelo: {car.altura}")
print(f"Tipo de vehiculo: {car.tipo}")
print(f"Cupo: {car.ocupantes}")

car.Acelerar()