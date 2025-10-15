
# Napisati program koji od korisnika
# čita 10 pozitivnih brojeva. Nakon toga program 
# ispisuje zbroj svih pozitivnih unesenih brojeva.

n = 0 # koliko je pozitivnih brojeva uneseno
z = 0 # zbroj

while n < 3:
    a = int(input("broj:"))
    if a > 0:
        z = z + a
        n = n + 1

print(z)