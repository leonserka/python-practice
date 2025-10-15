
# Korisnik unosi n, a program ispisuje pravokutan trokut n*n.

n = int(input("n:"))

for y in range(n):
    for x in range(y+1):
        print("*", end=" ")
    print()

'''
brojac = 1
for y in range(n):
    for x in range(brojac):
        print("*", end=" ")
    print()
    brojac += 1
'''