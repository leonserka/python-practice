
# N.f koja za neki broj vraća najbližu potenciju broja 2.
# Npr. za 15, vraća 16, za 10, vraća 8, itd.

def najbliza_pot2(broj):
    min_i = broj
    for i in range(broj):
        if abs(2**i - broj) < abs(2**min_i - broj):
            min_i = i
    return 2**min_i

print(najbliza_pot2(110))

