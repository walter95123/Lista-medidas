def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Entrada inválida. Escribí un número.")


def calcular(numero_1, numero_2, operacion):
    if operacion == "1":
        return numero_1 + numero_2
    if operacion == "2":
        return numero_1 - numero_2
    if operacion == "3":
        return numero_1 * numero_2
    if operacion == "4":
        if numero_2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return numero_1 / numero_2
    raise ValueError("Operación inválida.")


def main():
    print("=== Calculadora simple ===")

    while True:
        print("\n1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        operacion = input("Elegí una opción: ").strip()

        if operacion == "5":
            print("¡Hasta luego!")
            break

        if operacion not in {"1", "2", "3", "4"}:
            print("Opción inválida.")
            continue

        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")

        try:
            resultado = calcular(numero_1, numero_2, operacion)
            print(f"Resultado: {resultado:g}")
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
