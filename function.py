def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error:divison por cero"
    return a / b

def mostrar_menu():
    print("∖n 1. suma")
    print("2. resto")
    print("3. multiplicación")
    print("4. división")
    print("5. salir∖n")

def calculadora():
    while True:
        try:
            numero = int(input("Ingresar numero: "))
            numero_2 = int(input("Ingresar un segundo numero: "))
        except ValueError as e:
            print("Error")
            print("Detalle", e)
            continue
    
        mostrar_menu()
        opcion = input("Elegir una operación: ")

        if opcion == "1":
            print("Resultado:", sumar(numero, numero_2))
        elif opcion == "2":
            print("Resultado:", restar(numero, numero_2))
        elif opcion == "3":
            print("Resultado:", multiplicar(numero, numero_2))
        elif opcion == "4":
            print("Resultado:", division(numero, numero_2))
        elif opcion == "5":
            print("¡Adios!")
            break
        else:
                print("Opcion invalida. Intenta de nuevo.")

calculadora()