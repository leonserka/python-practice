
# Napisati funkcije za rad sa razlomcima:
#    množenje
#    dijeljenje
#    zbrajanje
#    oduzimanje

def pomnozi(a, b):
    ba, na = a
    bb, nb = b
    return (ba*bb, na*nb)

def podijeli(a, b):
    ba, na = a
    bb, nb = b
    return (ba*nb, na*bb)

def zbroji(a, b):
    ba, na = a
    bb, nb = b
    return (ba*nb + bb*na, na*nb)

def oduzmi(a, b):
    ba, na = a
    bb, nb = b
    return zbroji((ba, na), (-bb, nb))

x = (3, 4)
y = (1, 2)

r = pomnozi(x, y)    
print(r)