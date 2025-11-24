class Jugador:
    def __init__(self, nombre, dorsal):
        self.nombre = nombre
        self.dorsal = dorsal
        self.goles = 0
    def anotar_gol(self):
        self.goles += 1
    def resumen(self):
        return f"D-{self.dorsal} {self.nombre}  Goles: {self.goles}"
class Arquero(Jugador):
    def __init__(self, nombre, dorsal):
        super().__init__(nombre, dorsal)
        self.atajadas = 0
        self.goles_recibidos = 0
    def atajar(self):
        self.atajadas += 1
    def recibir_gol(self):
        self.goles_recibidos += 1
    def resumen(self):
        return f"D-{self.dorsal} {self.nombre}  Goles: {self.goles}, Atajadas: {self.atajadas}, Goles recibidos: {self.goles_recibidos}"
class Lateral(Jugador):
    def __init__(self, nombre, dorsal):
        super().__init__(nombre, dorsal)
        self.bloqueos = 0
    def bloquear(self):
        self.bloqueos += 1
    def resumen(self):
        return f"D-{self.dorsal} {self.nombre}  Goles: {self.goles}, Bloqueos: {self.bloqueos}"
class Armador(Jugador):
    def __init__(self, nombre, dorsal):
        super().__init__(nombre, dorsal)
        self.pases = 0
    def pasar(self):
        self.pases += 1
    def resumen(self):
        return f"D-{self.dorsal} {self.nombre}  Goles: {self.goles}, Pases: {self.pases}"
class Delantero(Jugador):
    def __init__(self, nombre, dorsal):
        super().__init__(nombre, dorsal)
        self.tiros = 0
    def tirar(self):
        self.tiros += 1
    def resumen(self):
        return f"D-{self.dorsal} {self.nombre}  Goles: {self.goles}, Tiros al arco: {self.tiros}"
arquero = Arquero("Arquero", 1)
lateralD = Lateral("Lateral D", 13)
lateralI = Lateral("Lateral I", 5)
armador = Armador("Armador", 69)
delantero = Delantero("Delantero", 7)
equipo = [arquero, lateralD, lateralI, armador, delantero]
while True:
    print("\nQUE SE VA A HACER")
    print("1. GOL")
    print("2. ATAJAR")
    print("3. BLOQUEO")
    print("4. PASE")
    print("5. TIRO AL ARCO")
    print("6. FINALIZAR PARTIDO")
    print("7. RECIBIR GOL")
    opc = input("Opción: ")
    if opc == "1":
        print("¿Quién hizo el gol?")
        for i, j in enumerate(equipo):
            print(f"{i+1}. {j.dorsal} — {j.nombre}")
        elegir = int(input("Jugador: ")) - 1
        equipo[elegir].anotar_gol()
        print("Gol!!!!!!!!!!!!!!!!!!!!!!!.")
    elif opc == "2":
        arquero.atajar()
        print("Ataja si señoras y señores!!!!.")
    elif opc == "3":
        print("1. Lateral 1\n2. Lateral 2")
        l = int(input("Cuál lateral bloqueo? "))
        if l == 1:
            lateralD.bloquear()
        else:
            lateralI.bloquear()
        print("Bloqueo.")
    elif opc == "4":
        armador.pasar()
        print("Pase, por la educacion!.")
    elif opc == "5":
        delantero.tirar()
        print("Tira y se vaaaaaaaaaaaaaaaa!!!!!!!.")
    elif opc == "7":
        arquero.recibir_gol()
        print("Se dejo hacer gol mucha lk")
    elif opc == "6":
        print("\nFILAN")
        total_goles = 0
        for j in equipo:
            print(j.resumen())
            total_goles += j.goles
        print(f"\nMARCADOR: EQUIPO {total_goles} — {arquero.goles_recibidos} RIVAL")
        break
    else:
        print("ERROR CAPA 8, OTRA VEZ.")
