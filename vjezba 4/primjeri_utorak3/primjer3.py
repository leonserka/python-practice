
# Napisati program koji od korisnika čita
# brojeve dok god korisnik ne unese 0. Tada
# program ispisuje zbroj svih unesenih brojeva.

z = 0
b = 1
while b != 0:
    b = int(input("broj:"))
    z += b

print(z)
