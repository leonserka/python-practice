
# Korisnik unosi n, a program ispisuje pravokutan trokut n*n.

n = int(input("n:"))

for y in range(n, 0, -1):
    for x in range(y):
        print("*", end=" ")
    print()

'''
for y in range(n):
    for x in range(n-y):
        print("*", end=" ")
    print()
'''