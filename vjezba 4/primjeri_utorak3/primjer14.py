
# Korisnik unosi n, a program ispisuje kvadrat n*n.

n = int(input("n:"))

for x in range(n):
    for y in range(n):
        print("*", end=" ")
    print()
