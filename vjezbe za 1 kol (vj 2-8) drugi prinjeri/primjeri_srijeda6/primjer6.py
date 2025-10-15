
# 4. Napisati program koji od korisnika čita (neparnu) visinu slova i zvjezdicama
# ispisuje slovo V.


n = 9

# *......*   0  0  6
# .*....*    1  1  4
# ..*..*     2     2
# ...**      3     0

def linija(brp, brs):
    for i in range(brp):    
        print(".", end=" ")
    print("*", end=" ")
    for i in range(brs):    
        print(".", end=" ")
    print("*")
        
for y in range(n):
    linija(y, 2*n - 2 - 2*y)

'''
for y in range(n):
    for x in range(n*2):
        if x == y or x == 2*n - y - 1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
'''        