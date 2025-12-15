"""
Archivo principal para comparar Programación Tradicional vs POO.

Este módulo permite al usuario elegir entre ejecutar el programa de cálculo
del promedio semanal del clima usando Programación Tradicional o
Programación Orientada a Objetos (POO).

Autor: Leonardo Cordova
Fecha: 2025
Asignatura: Programación Orientada a Objetos
"""

# Importar los módulos de ambos enfoques
import clima_tradicional
import clima_poo


def mostrar_menu() -> int:
    """
    Muestra el menú principal y solicita la opción del usuario.

    Returns:
        int: Opción seleccionada por el usuario (1, 2 o 3).
    """
    print("\n" + "=" * 60)
    print("  SISTEMA DE CÁLCULO DE PROMEDIO SEMANAL DEL CLIMA")
    print("=" * 60)
    print("\nSeleccione el enfoque de programación:")
    print("1. Programación Tradicional (Funciones)")
    print("2. Programación Orientada a Objetos (POO)")
    print("3. Salir")
    print("-" * 60)

    while True:
        try:
            opcion = int(input("Ingrese su opción (1-3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Error: Por favor ingrese una opción válida (1, 2 o 3).")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")


def main() -> None:
    """
    Función principal del programa.

    Controla el flujo del programa, mostrando el menú y ejecutando
    la opción seleccionada por el usuario hasta que decida salir.
    """
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            # Ejecutar versión con Programación Tradicional
            print("\n>>> Ejecutando Programación Tradicional <<<")
            clima_tradicional.ejecutar_programa_tradicional()

        elif opcion == 2:
            # Ejecutar versión con POO
            print("\n>>> Ejecutando Programación Orientada a Objetos <<<")
            clima_poo.ejecutar_programa_poo()

        elif opcion == 3:
            # Salir del programa
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break

        # Pausa antes de volver al menú
        input("\nPresione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()