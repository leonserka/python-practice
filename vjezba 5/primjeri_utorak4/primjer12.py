
# Korisnik unosi 4 broja, program
# ispisuje zbroj najveceg i najmanjeg broja.

def maks(a, b):
    if a > b:
        return a
    else:
        return b

def mini(a, b):
    if a > b:
        return b
    else:
        return a

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

#x = maks(a, b)
#y = maks(c, d)
#najveci = maks(x, y)
najveci = maks(maks(a, b), maks(c, d))
najmanji = mini(mini(a, b), mini(c, d))
print(najveci-najmanji)

