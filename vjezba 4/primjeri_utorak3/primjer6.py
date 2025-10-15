
# Napisati program koji od korisnika
# čita 10 brojeva. Nakon toga program 
# ispisuje zbroj svih pozitivnih unesenih brojeva.

z = 0
for i in range(5):
    a = int(input("broj:"))
    if a > 0:
        z = z + a

print(z)
    