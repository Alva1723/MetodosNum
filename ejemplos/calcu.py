while True:
    print("\n=== CALCULADORA BÁSICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Programa finalizado.")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcion == "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)

    except ValueError:
        print("Error: Debes ingresar únicamente números.")