import math


a = float(input("Unesite duljinu prve katete: "))
b = float(input("Unesite duljinu druge katete: "))
# Računanje hipotenuze
c = math.sqrt(a**2 + b**2)


print("Hipotenuza pravokutnog trokuta s katetama  je ",c)
