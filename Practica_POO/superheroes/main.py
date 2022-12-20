from superheroe import Superheroe
from arma import Arma

katana = Arma("Katana", 7, 4, 9)
cuchillas = Arma("Cuchillas", 5, 3, 8)

deadpool    = Superheroe("Deadpool", 20, 5, True, katana)
wolverine   = Superheroe("Wolverine", 20, 7, False, cuchillas)

print("Salud de DeadPool", deadpool.salud)
wolverine.atacar(deadpool)

print("Salud de DeadPool", deadpool.salud)

print("Resistencia de la katana", katana.resistencia)