def koord(x,y,z):
    if x>y:
        x,y=y,x
    if y>z:
        y,z=z,y
    if x>y:
        x,y=y,x
    return x,y

x = float(input("Unesite koordinatu x: "))
y = float(input("Unesite koordinatu y: "))
z = float(input("Unesite koordinatu z: "))

print("2D kordinate : ", koord(x,y,z) )

