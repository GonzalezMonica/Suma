class Suma:
  def __init__(self):
      try:
          self.num1=float(input("Ingresa un numero: "))
          self.num2=float(input("Ingresa otro numero: "))
          self.suma=self.num1+self.num2
          print("Tu resultado es: ", self.suma)
      except ValueError:
          print("ERROR: Solo se permiten numeros. ")   
s=Suma()
