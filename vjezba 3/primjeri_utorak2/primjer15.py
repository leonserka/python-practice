
# Korisnik upiše dvije katete i hipotenuzu
# u bilo kojem redoslijedu
# i program kaže da li je taj trokut pravokutan.
# U slucaju da korisnik ne upiše pozitivne brojeve,
# program ispisuje grešku
# c**2 = a**2 + b**2

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > 0 and b > 0 and c > 0:
    # zamjene tako da je hipotenuza u c
    # dodatna varijabla
    if c >= a and c >= b:
        hip = c
        k1 = a
        k2 = b
    elif a >= c and a >= b:
        hip = a
        k1 = c
        k2 = b
    else: #elif b >= a and b >= c:
        hip = b
        k1 = a
        k2 = c
    
    if hip**2 == k1**2 + k2**2:
        print("pravokutan")
    else:
        print("nije pravokutan")
else:
    print("greška")