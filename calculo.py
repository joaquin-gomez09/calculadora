while True:
    numero = int(input("Ingresar un numero:"))
    numero_2 = int(input("Ingresar un segundo numero:"))

    print("")
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. división")
    print("5. salir")
    print("")

    try: 
        opcion = input("Elegir una operación: ")
    except ValueError as e:
        print("error")
        print("detalle:", e)
        continue

    if opcion == "1":
        try:
            resultado = numero + numero_2
            print(resultado)
        except ValueError as e:
            print("error")
            print("detalle:", e)
    
    elif opcion == "2":
        try:
            resultado = numero - numero_2
            print(resultado)
        except ValueError as e:
            print("error")
            print("detalle:", e)

    elif opcion == "3":
        try:
            resultado = numero * numero_2
            print(resultado)
        except ValueError as e:
            print("error")
            print("detalle:", e)

    elif opcion == "4":
        try:
            resultado = numero / numero_2
            print(resultado)
        except ValueError as e:
            print("error")
            print("detalle:", e)
    
    elif opcion == "5":
        break