
# 2. Napisati program koji zvjezdicama ispisuje dva kvadrata.
# Kvadrati su postavljeni dijagonalno (dolje-lijevo i gore-desno).
# Dužinu stranice kvadrata zadaje korisnik.

# ---***
# ---***
# ---***

# ***
# ***
# ***

def linija(brr, brz):
    for i in range(brr):
        print(".", end=" ")
    for i in range(brz):
        print("*", end=" ")
    print()

n = int(input("duzina: "))
for i in range(n//2):
    linija(n // 2, n // 2)
for i in range(n//2):
    linija(0, n // 2)



'''
n = int(input("duzina: "))
for y in range(n):
    for x in range(n):
        if x >= n // 2 and y < n // 2:
            print("*", end=" ")
        elif x < n // 2 and y >= n // 2:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
'''