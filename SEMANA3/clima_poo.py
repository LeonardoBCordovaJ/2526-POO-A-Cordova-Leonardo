"""
Módulo de Programación Orientada a Objetos para calcular el promedio semanal del clima.

Este módulo utiliza clases y objetos para encapsular la información del clima
y proporcionar métodos para gestionar temperaturas y calcular promedios.
"""

from typing import List


class ClimaDiario:
    """
    Representa la información del clima de un día específico.

    Esta clase encapsula los datos de temperatura de un solo día,
    permitiendo una mejor organización y reutilización del código.

    Atributos:
        dia (str): Nombre del día de la semana.
        temperatura (float): Temperatura registrada en grados Celsius.
    """

    def __init__(self, dia: str, temperatura: float) -> None:
        """
        Inicializa un objeto ClimaDiario con el día y su temperatura.

        Args:
            dia: Nombre del día de la semana.
            temperatura: Temperatura en grados Celsius.
        """
        self.__dia = dia  # Atributo privado (encapsulamiento)
        self.__temperatura = temperatura  # Atributo privado

    # Métodos getter para acceder a los atributos privados
    def get_dia(self) -> str:
        """Retorna el nombre del día."""
        return self.__dia

    def get_temperatura(self) -> float:
        """Retorna la temperatura del día."""
        return self.__temperatura

    # Métodos setter para modificar la temperatura
    def set_temperatura(self, nueva_temperatura: float) -> None:
        """
        Modifica la temperatura del día.

        Args:
            nueva_temperatura: Nueva temperatura en grados Celsius.
        """
        self.__temperatura = nueva_temperatura

    def __str__(self) -> str:
        """
        Representación en cadena del objeto ClimaDiario.

        Returns:
            str: Descripción legible del clima del día.
        """
        return f"{self.__dia}: {self.__temperatura}°C"


class ClimaSemanal:
    """
    Gestiona la información del clima de toda una semana.

    Esta clase permite ingresar temperaturas diarias, calcular el promedio
    semanal y obtener estadísticas adicionales del clima.

    Atributos:
        dias_clima (List[ClimaDiario]): Lista de objetos ClimaDiario.
    """

    def __init__(self) -> None:
        """Inicializa un objeto ClimaSemanal con una lista vacía de días."""
        self.__dias_clima: List[ClimaDiario] = []

    def ingresar_temperaturas(self) -> None:
        """
        Solicita al usuario ingresar las temperaturas de cada día de la semana.

        Crea objetos ClimaDiario para cada día y los almacena en la lista.
        """
        print("\n=== Ingreso de Temperaturas Diarias (POO) ===")
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        self.__dias_clima = []  # Reiniciar la lista

        for dia in dias:
            while True:
                try:
                    # Solicitar temperatura y validar entrada
                    temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                    # Crear objeto ClimaDiario y agregarlo a la lista
                    clima_dia = ClimaDiario(dia, temp)
                    self.__dias_clima.append(clima_dia)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un valor numérico válido.")

    def calcular_promedio(self) -> float:
        """
        Calcula el promedio de las temperaturas de la semana.

        Returns:
            float: Promedio de temperaturas. Retorna 0 si no hay datos.
        """
        if len(self.__dias_clima) == 0:
            return 0

        # Sumar todas las temperaturas usando los métodos getter
        suma = sum(dia.get_temperatura() for dia in self.__dias_clima)
        promedio = suma / len(self.__dias_clima)

        return promedio

    def obtener_temperatura_maxima(self) -> float:
        """
        Obtiene la temperatura máxima de la semana.

        Returns:
            float: Temperatura máxima registrada.
        """
        if not self.__dias_clima:
            return 0
        return max(dia.get_temperatura() for dia in self.__dias_clima)

    def obtener_temperatura_minima(self) -> float:
        """
        Obtiene la temperatura mínima de la semana.

        Returns:
            float: Temperatura mínima registrada.
        """
        if not self.__dias_clima:
            return 0
        return min(dia.get_temperatura() for dia in self.__dias_clima)

    def mostrar_resultados(self) -> None:
        """
        Muestra un resumen completo de las temperaturas y estadísticas.

        Presenta cada día con su temperatura, el promedio semanal,
        y las temperaturas máxima y mínima.
        """
        print("\n=== Resultados (POO) ===")
        print("Temperaturas de la semana:")

        # Mostrar cada día usando el métodos __str__ de ClimaDiario
        for clima in self.__dias_clima:
            print(f"  - {clima}")

        # Mostrar estadísticas
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal: {promedio:.2f}°C")
        print(f"Temperatura máxima: {self.obtener_temperatura_maxima():.2f}°C")
        print(f"Temperatura mínima: {self.obtener_temperatura_minima():.2f}°C")


def ejecutar_programa_poo():
    """
    Función principal que ejecuta el programa completo usando POO.

    Crea una instancia de ClimaSemanal y coordina la entrada de datos
    y la presentación de resultados.
    """
    clima_semana = ClimaSemanal()
    clima_semana.ingresar_temperaturas()
    clima_semana.mostrar_resultados()


# Bloque de ejecución directa
if __name__ == "__main__":
    ejecutar_programa_poo()