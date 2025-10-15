
def pomnozi(ra, rb):
    ab, an = ra
    bb, bn = rb
    return (ab*bb, an*bn)

def podijeli(ra, rb):
    ab, an = ra
    bb, bn = rb
    return (ab*bn, an*bb)

def zbroji(ra, rb):
    ab, an = ra
    bb, bn = rb
    return (ab*bn+bb*an, an*bn)

def oduzmi(ra, rb):
    ab, an = ra
    bb, bn = rb
    return zbroji((ab, an), (-bb, bn))

x = (2, 3)
y = (1, 2)

rc = pomnozi(x, y)
print(rc)
