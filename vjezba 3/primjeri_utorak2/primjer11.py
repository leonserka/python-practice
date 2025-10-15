
# Korisnik upiše dvije katete i hipotenuzu
# i program kaže da li je taj trokut pravokutan.

# c**2 = a**2 + b**2

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if c**2 == a**2 + b**2:
    print("pravokutan")
else:
    print("nije pravokutan")
