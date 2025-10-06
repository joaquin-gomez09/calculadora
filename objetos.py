class Calculadora:
    def __init__(self):
        self.numero = 0
        self.numero_2 = 0
        self.opcion = ""
    
    def ingresar_numeros(self):
        try:
            self.numero = int(input("Ingresa un numero:"))
            self.numero_2 = int(input("Ingresa un segundo numero:"))
        except ValueError:
            print("Por favor, ingresa solo numeros")
            self.ingresar_numeros()

    def elegir_opcion(self):
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
    
    def operacion(self):
        try:
            if self.opcion == "1":
                print("Resultado: ", self.numero + self.numero_2)
            elif self.opcion == "2":
                print("Resultado: ", self.numero - self.numero_2)
            elif self.opcion == "3":
                print("Resultado: ", self.numero * self.numero_2)
            elif self.opcion == "4":
                if self.opcion != 0:
                    print("Resultado: ", self.numero / self.numero_2)
                else:
                    print("Error: división por cero.")
            elif self.opcion == 5:
                print("¡Adios!")
                return False
            else:
                print("Opción invalida")
        except Exception as e:
            print("Error en la operación: ", e)
        return True
    
    def iniciar(self):
        while True:
            self.ingresar_numeros()
            self.elegir_opcion()
            self.opcion = input("Elegir una operación:")
            if not self.operacion():
                break

calculadora = Calculadora()
calculadora.iniciar()