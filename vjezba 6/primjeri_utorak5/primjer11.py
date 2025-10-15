
# N.f. koja ispisuje sve brojeve od a do b.
# a i b mogu biti u bilo kojem redoslijedu, ispisujemo 
# od manjeg do veceg

def ispisi(a, b):
    if a > b:
        b, a = a, b
    for i in range(a, b):
        print(i)
    
def ispisi2(a, b):
    if a > b:
        b, a = a, b
    while a < b:
        print(a)
        a += 1

def ispisi_rek(a, b):
    if a > b:
        ispisi_rek(b, a)
        return
    if a == b:
        return
    print(a)
    ispisi_rek(a+1, b)

ispisi(3, 7)
ispisi(7, 3)