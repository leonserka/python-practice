# Korisnik unosi n, a program ispisuje pravokutan trokut n*n.

n = int(input("n:"))

for y in range(n):
    for x in range(n-y-1):
        print(".", end=" ")
    for x in range(y+1):
        print("*", end=" ")            
    print()

'''
brr = n-1
brz = 1
for y in range(n):
    for x in range(brr):
        print(".", end=" ")
    for x in range(brz):
        print("*", end=" ")            
    print()
    brr -= 1
    brz += 1

'''

'''
for y in range(n):
    for x in range(n):
        if x >= (n-y):
            print("*", end=" ")
        else:
            print(".", end=" ")            
    print()
'''
'''
for y in range(n):
    for x in range(n-y):
        print("*", end=" ")
    print()
'''