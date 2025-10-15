
# N.f. koja vraća najveci.z.d. za dva broja.

def nzd(a, b):
    nd = 1
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            nd = i
    return nd

def nzd_rek(a, b):
    if a == b:
        return a
    if a > b:
        return nzd_rek(a-b, b)
    if a < b:
        return nzd_rek(a, b-a)
    
print(nzd(24, 36))
print(nzd_rek(24, 36))