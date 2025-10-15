
# Napisati program koji zvjezdicama iscrtava prazan pravokutni
# trokut (katete su postavljene kao L). Katete su jednake dužine,
# zadane od korisnika. Zadatak rješiti petljama i pomoćnom
# funkcijom za iscrtavanje N razmaka (napisati funkciju).

# *

# *.*    0 1
# *..*   1 2
# *...*

# ******

def razmaci(brr):
    for i in range(brr):
        print(".", end=" ")

n = 10
print("*")

for i in range(n-2):
    print("*", end=" ")
    razmaci(i)
    print("*")

for i in range(n):
    print("*", end=" ")


