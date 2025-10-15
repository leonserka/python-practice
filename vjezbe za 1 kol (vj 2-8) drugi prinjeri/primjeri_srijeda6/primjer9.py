
# 4. Napisati rekurzivnu funkciju koja ispisuje sve brojeve između dva broja koja
# dobije kao parametre.

def ispisi(a, b):
    if a > b:
        a, b = b, a
    while a < b:
        print(a)
        a += 1

def ispisi_rek(a, b):
    if a > b:
        a, b = b, a
    if a == b:
        return
    print(a)    
    ispisi_rek(a+1, b)

ispisi_rek(20, 10)    
