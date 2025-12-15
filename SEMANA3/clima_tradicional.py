"""
Módulo de Programación Tradicional para calcular el promedio semanal del clima.

Este módulo utiliza funciones para gestionar la entrada de temperaturas diarias
y calcular el promedio semanal sin utilizar clases ni objetos.
"""

# Variable global para almacenar las temperaturas de la semana
temperaturas_semanales = []


def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias de una semana.

    Esta función pide 7 temperaturas (una por cada día de la semana) y las
    almacena en la lista global 'temperaturas_semanales'.
    """
    global temperaturas_semanales
    temperaturas_semanales = []  # Reiniciar la lista

    print("\n=== Ingreso de Temperaturas Diarias (Programación Tradicional) ===")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        while True:
            try:
                # Solicitar temperatura y validar que sea un número
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas_semanales.append(temp)
                break
            except ValueError:
                print("Error: Por favor ingrese un valor numérico válido.")


def calcular_promedio():
    """
    Calcula el promedio de las temperaturas ingresadas.

    Returns:
        float: El promedio de las temperaturas de la semana.
               Retorna 0 si no hay temperaturas registradas.
    """
    if len(temperaturas_semanales) == 0:
        return 0

    # Sumar todas las temperaturas y dividir por la cantidad de días
    suma_temperaturas = sum(temperaturas_semanales)
    promedio = suma_temperaturas / len(temperaturas_semanales)

    return promedio


def mostrar_resultados():
    """
    Muestra las temperaturas ingresadas y el promedio semanal calculado.

    Esta función presenta un resumen completo de los datos ingresados
    y el resultado del cálculo del promedio.
    """
    print("\n=== Resultados (Programación Tradicional) ===")
    print("Temperaturas de la semana:", temperaturas_semanales)

    promedio = calcular_promedio()
    print(f"Promedio semanal: {promedio:.2f}°C")

    # Información adicional: temperatura máxima y mínima
    if temperaturas_semanales:
        print(f"Temperatura máxima: {max(temperaturas_semanales):.2f}°C")
        print(f"Temperatura mínima: {min(temperaturas_semanales):.2f}°C")


def ejecutar_programa_tradicional():
    """
    Función principal que ejecuta el programa completo en modo tradicional.

    Coordina la entrada de datos, el cálculo y la presentación de resultados.
    """
    ingresar_temperaturas()
    mostrar_resultados()


# Bloque de ejecución directa (solo si se ejecuta este archivo directamente)
if __name__ == "__main__":
    ejecutar_programa_tradicional()