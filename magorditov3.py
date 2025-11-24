class magordito: 
    def __init__(self, nombre, edad, genero, caracterizacion, ocupacion,
                 equipo_especial, vidas, resistencia, habilidades, oficio,
                 poder_equipo, tipo_arma, daño):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.caracterizacion = caracterizacion
        self.ocupacion = ocupacion
        self.equipo_especial = equipo_especial
        self.vidas = vidas
        self.resistencia = resistencia
        self.habilidades = habilidades
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.tipo_arma = tipo_arma
        self.daño = daño
    def hablar(self):
        print(f"{self.nombre} dice: Hola! Soy Halfonso, soy El {self.ocupacion} Primordial y Arquimago Universal del Tiempo y la Realidad, maximo exponente y consejero.")
    def talk(self):
        print(f"\ny no se que mas poner, pronto nuevos avances.")

hlf = magordito(
    nombre = "Halfonso",
    edad = "200",
    genero = "Primordial y Arquimago Universal del Tiempo y la Realidad.",
    caracterizacion = "consejero",
    ocupacion = "Mago",
    equipo_especial = "Batamanta Arcana del Destino",
    vidas = 3,
    resistencia = "Resistencia mística 5000",
    habilidades = ["Control Temporal", "Desgarro de Realidad", "Conjuro Primigenio"],
    oficio = "consejero",
    poder_equipo = "Amplificación 70% del poder ",
    tipo_arma = "Báculo del Eterno Retorno",
    daño = "Daño cósmico clase X"
)
print(f"Mi nombre es: {hlf.nombre}")
print(f"Tengo {hlf.edad} Niveles de experiencia y ahora soy")
print(f"EL {hlf.genero}")
print(f"Soy: {hlf.caracterizacion}")
print(f"Y tambien {hlf.ocupacion} de decima categoria. El {hlf.ocupacion} Absoluto mas poderoso en todo el reino")
print(f"Equipo especial: {hlf.equipo_especial}")
print(f"Vidas: {hlf.vidas}")
print(f"Resistencia: {hlf.resistencia}")
print(f"Habilidades: {', '.join(hlf.habilidades)}")
print(f"Oficio: {hlf.oficio}")
print(f"Poder del equipo: {hlf.poder_equipo}")
print(f"Tipo de arma: {hlf.tipo_arma}")
print(f"Daño: {hlf.daño}")
hlf.hablar()
hlf.talk()
class NPC(magordito):
    def __init__(self, nombre, edad, genero, caracterizacion, ocupacion,
                 equipo_especial, vidas, resistencia, habilidades, oficio,
                 poder_equipo, tipo_arma, daño, tablero):
        super().__init__(nombre, edad, genero, caracterizacion, ocupacion,
                         equipo_especial, vidas, resistencia, habilidades,
                         oficio, poder_equipo, tipo_arma, daño)
        self.tablero = tablero  
    def pedido(self):
        print("\n Ausencia de oscuridad ")
        for clave, valor in self.tablero.items():
            print(f"{clave}: {valor}")
    def presentarse(self):
        print(f"\nSoy {self.nombre}, el fiel acompañante de Halfonso. ")
npc = NPC(
    nombre = "Ausencia de oscuridad",
    edad = "340 años",
    genero = "troll",
    caracterizacion = "Leal, gruñón",
    ocupacion = "Guerrero",
    equipo_especial = "Casco de Hierro",
    vidas = 2,
    resistencia = "100 puntos",
    habilidades = ["Golpe sísmico", "super fuerza"],
    oficio = "Herrero",
    poder_equipo = "Aumenta su defensa en 200%",
    tipo_arma = "palo de madera con moho",
    daño = "Daño contundente y un daño extra contra criaturas subterráneas",
    tablero = {
        "misión_actual": "Proteger a Halfonso",
        "nivel_confianza": "Máximo",
        "ubicación": "muy muy lejano",
        "estado": "preparado para el combate"
    }
)
npc.presentarse()
npc.pedido()
