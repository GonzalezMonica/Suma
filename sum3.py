class Suma:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0

    def pedir_numeros(self):
        try:
            self.numero1 = float(input("Introduce el primer número: "))
            self.numero2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: Solo se permiten números. Inténtalo de nuevo.")
            return False
        return True

    def calcular_suma(self):
        return self.numero1 + self.numero2

s = Suma()
if s.pedir_numeros():
    resultado = s.calcular_suma()
    print("La suma es:", resultado)