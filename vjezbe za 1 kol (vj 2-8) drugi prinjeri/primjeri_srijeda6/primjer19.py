
# N.f koja za neki broj vraća najbliži kvadrat cijelog broja.
# Npr. za 15, vraća 16, za 10, vraća 9, itd.

def najblizi_kvadrat(broj):
    min_i = broj
    for i in range(broj):
        if abs(i*i - broj) < abs(min_i*min_i - broj):
            min_i = i
    return min_i*min_i

print(najblizi_kvadrat(80))

