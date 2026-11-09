import random
import math


def solicitar_positivo(mensaje):
    """Solicita un número decimal positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


def solicitar_entero_positivo(mensaje):
    """Solicita una cantidad entera positiva de puntos."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")


def main():
    print("=== Cálculo del área de intersección mediante Montecarlo ===")

    # Solicitar las constantes de las ecuaciones
    a = solicitar_positivo("Ingresa el valor de a (elipse): ")
    b = solicitar_positivo("Ingresa el valor de b (elipse): ")
    c = solicitar_positivo("Ingresa el valor de c (hipérbola): ")
    d = solicitar_positivo("Ingresa el valor de d (hipérbola): ")

    cantidad_puntos = solicitar_entero_positivo(
        "¿Cuántos puntos aleatorios deseas generar?: "
    )

    puntos_en_elipse = 0
    puntos_en_interseccion = 0

    # Generar puntos dentro del rectángulo [-a, a] x [-b, b]
    for _ in range(cantidad_puntos):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        # Comprobar si el punto pertenece a la elipse
        pertenece_elipse = (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1

        if pertenece_elipse:
            puntos_en_elipse += 1

            # Comprobar si también pertenece a la región de la hipérbola
            pertenece_hiperbola = (x ** 2 / c ** 2) - (y ** 2 / d ** 2) >= 1

            if pertenece_hiperbola:
                puntos_en_interseccion += 1

    # Área de la elipse
    area_elipse = math.pi * a * b

    # Área de la intersección
    if puntos_en_elipse > 0:
        proporcion = puntos_en_interseccion / puntos_en_elipse
        area_interseccion = proporcion * area_elipse
    else:
        proporcion = 0
        area_interseccion = 0

    # Mostrar resultados
    print("\n========== RESULTADOS ==========")
    print(f"Puntos aleatorios generados: {cantidad_puntos}")
    print(f"Puntos dentro de la elipse: {puntos_en_elipse}")
    print(f"Puntos en la intersección: {puntos_en_interseccion}")
    print(f"Área de la elipse: {area_elipse:.6f}")
    print(f"Proporción de intersección: {proporcion:.6f}")
    print(f"Área aproximada de la intersección: {area_interseccion:.6f}")


if __name__ == "__main__":
    main()