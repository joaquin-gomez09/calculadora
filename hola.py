raw = input("Ingresa algo: ")
#limpio = raw.strip()
print(raw)

    
opcion = input("elige una opcion: ")

try:
    num_1 = float(input("Ingresar un numero: "))
    num_2 = float(input("Ingresar un numero: "))

    print(num_1 + num_2)
except ValueError as e:
    print("Error")
    print("Detalle:", e)