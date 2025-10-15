
# Napisati funkciju koja prima dva broja i vraća najveći i najmanji
# zajednički djelitelj njih dvoje, veći od 1.

def djelitelji(a, b):
    najmanji = 0
    najveci = 0
    for d in range(2, a+1):
        if a % d == 0 and b % d == 0:
            najveci = d
            if najmanji == 0:
                najmanji = d
    return najmanji, najveci

print(djelitelji(128, 64))
            
            