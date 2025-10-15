
# N.f. koja ispisuje sve brojeve od a do b.

def ispisi(a, b):
    for i in range(a, b):
        print(i)
    
def ispisi2(a, b):
    while a < b:
        print(a)
        a += 1

def ispisi_rek(a, b):
    if a == b:
        return
    print(a)
    ispisi_rek(a+1, b)

ispisi_rek(3, 7)