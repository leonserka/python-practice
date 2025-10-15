
# Korisnik unosi 10 brojeva. Program ispisuje najmanji uneseni broj.

m = int(input("Broj:"))
for i in range(9):
    a = int(input("Broj:"))
    if a < m:
        m = a

print(m)