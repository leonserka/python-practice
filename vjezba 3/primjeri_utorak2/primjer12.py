
# Korisnik upiše dvije katete i hipotenuzu
# i program kaže da li je taj trokut pravokutan.
# U slucaju da korisnik ne upiše pozitivne brojeve,
# program ispisuje grešku i ne računa ništa.

# c**2 = a**2 + b**2

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > 0 and b > 0 and c > 0:
    if c**2 == a**2 + b**2:
        print("pravokutan")
    else:
        print("nije pravokutan")
else:
    print("greska")