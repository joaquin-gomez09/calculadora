class Calculadora:
    def __init__(self):
        self.numero = 0
        self.numero = 0
    
    def ingresar_numeros(self):
        self.numero = int(input("Ingresar un número: "))
        self.numero_2 = int(input("Ingresar un segundo numero:"))
    
    def mostrar_menu(self):
        print("1. suma")
        print("2. resta")
        print("3. multiplicación")
        print("4. división")
        print("5. salir")

    def operar(self, opcion):
        try:
            if opcion == "1":
                print("Resultado:", self.numero + self.numero_2)
            elif opcion == "2":
                print("Resultado:", self.numero - self.numero_2)
            elif opcion == "3":
                print("Resultado:", self.numero * self.numero_2)
            elif opcion == "4":
                print("Resultado:", self.numero / self.numero_2)
            elif opcion == "5":
                print("!Adios¡")
                return False
            else:
                print("opción invalida")
        except Exception as e:
            print("Error", e)
        return True
    
    def iniciar(self):
        while True:
            self.ingresar_numeros()
            self.mostrar_menu()
            opcion = input("Elegir una operación:")
            if not self.operar(opcion):
                break

calculadora = Calculadora()
calculadora.iniciar()