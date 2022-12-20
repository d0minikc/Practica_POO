#CLASE CON METODO

class Coche: 
    def __init__ (self, marca, modelo):
        self.marca      = marca
        self.modelo     = modelo
        self.arrancado  = False
        
# CLASE CON METODO STR
    def __str__ (self):
        return "El coche es: " + self.marca + " " + self.modelo
    
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")
    
          
    def parar(self):
        self.parar = False
        print("El", self.marca, self.modelo, "se ha parado")
        
ferrari = Coche("Ferrari", "F40")
tesla   = Coche("Tesla", "Model 3")

print(type(ferrari))
print(type(tesla))

print(ferrari.marca, ferrari.modelo)
print(tesla.marca, tesla.modelo)

ferrari.arrancar()
tesla.arrancar()

print(ferrari.arrancado)
print(tesla.arrancado)

ferrari.parar()
tesla.parar()

print(ferrari.parar)
print(tesla.parar)     

#METODO STR
print(ferrari)
print(tesla)