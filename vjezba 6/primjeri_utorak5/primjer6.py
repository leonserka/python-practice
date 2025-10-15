
# N.f. koja računa n-tu potenciju broja 3. (iter i rek)

def potencija(n):
    p = 1
    for i in range(n):
        p = p * 3
    return p

def potencija_rek(n):
    # temeljni slucaj
    if n == 0:
        return 1
    # rekurzivni slucaj
    return potencija_rek(n-1) * 3

print(potencija(4))

print(potencija_rek(4))