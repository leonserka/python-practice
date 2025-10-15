
# *********   0 2*n
# .*******    1 2*n-2
# ..*****     2 2*n-4
# ...***
# ....*

def linija(brr, brz):
    for i in range(brr):
        print(".", end=" ")
    for i in range(brz):
        print("*", end=" ")
    print()
    
n = 5
for i in range(n):
    linija(i, 2*n - 2*i - 1)