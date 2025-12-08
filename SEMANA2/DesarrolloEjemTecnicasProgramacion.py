class Vehiculo:

    def __init__(self, modelo, velocidad, aceleracion, resistencia, combustible):
        self.modelo = modelo
        self.velocidad = velocidad
        self.aceleracion = aceleracion
        self.resistencia = resistencia
        self.combustible = combustible

    def especificaciones(self):
        print(self.modelo, ":", sep="")
        print("·Velocidad:", self.velocidad)
        print("·Aceleración:", self.aceleracion)
        print("·Resistencia:", self.resistencia)
        print("·Combustible:", self.combustible)

    def mejorar_vehiculo(self, velocidad, aceleracion, resistencia):
        self.velocidad = self.velocidad + velocidad
        self.aceleracion = self.aceleracion + aceleracion
        self.resistencia = self.resistencia + resistencia

    def en_carrera(self):
        return self.combustible > 0

    def abandonar(self):
        self.combustible = 0
        print(self.modelo, "se ha quedado sin combustible y abandona")

    def impacto(self, rival):
        return self.velocidad - rival.resistencia

    def adelantar(self, rival):
        daño = self.impacto(rival)
        rival.combustible = rival.combustible - daño
        print(self.modelo, "ha impactado con", daño, "puntos de daño a", rival.modelo)
        if rival.en_carrera():
            print("Combustible de", rival.modelo, "es", rival.combustible)
        else:
            rival.abandonar()


class AutoDeportivo(Vehiculo):

    def __init__(self, modelo, velocidad, aceleracion, resistencia, combustible, turbo):
        super().__init__(modelo, velocidad, aceleracion, resistencia, combustible)
        self.turbo = turbo

    def cambiar_turbo(self):
        opcion = int(input("Elige un turbo: (1) Turbo básico, potencia 5. (2) Turbo avanzado, potencia 8: "))
        if opcion == 1:
            self.turbo = 5
        elif opcion == 2:
            self.turbo = 8
        else:
            print("Opción de turbo incorrecta")

    def especificaciones(self):
        super().especificaciones()
        print("·Turbo:", self.turbo)

    def impacto(self, rival):
        return self.velocidad * self.turbo - rival.resistencia


class Camioneta(Vehiculo):

    def __init__(self, modelo, velocidad, aceleracion, resistencia, combustible, blindaje):
        super().__init__(modelo, velocidad, aceleracion, resistencia, combustible)
        self.blindaje = blindaje

    def especificaciones(self):
        super().especificaciones()
        print("·Blindaje:", self.blindaje)

    def impacto(self, rival):
        return self.aceleracion * self.blindaje - rival.resistencia


def carrera(vehiculo_1, vehiculo_2):
    vuelta = 1
    while vehiculo_1.en_carrera() and vehiculo_2.en_carrera():
        print("\n========================= Vuelta", vuelta, "=========================")
        print(">>> Acción de", vehiculo_1.modelo, ":", sep="")
        vehiculo_1.adelantar(vehiculo_2)
        print(">>> Acción de", vehiculo_2.modelo, ":", sep="")
        vehiculo_2.adelantar(vehiculo_1)
        vuelta = vuelta + 1

    print("\n=========================== Fin de la carrera ===========================")
    if vehiculo_1.en_carrera():
        print("Ha ganado", vehiculo_1.modelo)
    elif vehiculo_2.en_carrera():
        print("Ha ganado", vehiculo_2.modelo)
    else:
        print("Empate")


# Crear vehículos
vehiculo_1 = AutoDeportivo("Ferrari F40", 25, 12, 3, 100, 6)
vehiculo_2 = Camioneta("Monster Truck", 8, 18, 5, 120, 4)

vehiculo_1.especificaciones()
print()
vehiculo_2.especificaciones()

carrera(vehiculo_1, vehiculo_2)
