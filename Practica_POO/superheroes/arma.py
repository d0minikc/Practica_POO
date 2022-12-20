class Arma:
    
    def __init__(self, nombre, resistencia, destruccion, daño):
        self.nombre         = nombre
        self.resistencia    = resistencia       
        self.destruccion    = destruccion           
        self.daño           = daño
       
        
    def __str__(self):
        return self.nombre
        
        