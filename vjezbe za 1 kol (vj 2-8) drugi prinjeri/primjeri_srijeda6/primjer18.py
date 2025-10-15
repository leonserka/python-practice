
# N.f. koja pretvara 3D koordinatu u 2D koordinatu tako
# da uzme dva najmanja elementa 3D koordinate.

def d3ud2(koo):
    x, y, z = koo
    if x >= y and x >= z:
        return (y, z)
    if y >= x and y >= z:
        return (x, z)
    if z >= y and z >= x:
        return (x, y)
    return (x, z)
        
k = (2, 1, 3)
print(d3ud2(k))

k = (4, 1, 3)
print(d3ud2(k))

k = (2, 5, 3)
print(d3ud2(k))