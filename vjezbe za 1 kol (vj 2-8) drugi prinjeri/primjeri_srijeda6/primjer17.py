
# Napisati rekurzivnu funkciju koja prima jedan broj i vraća
# koliko znamenki broja je djeljivo sa 3. Na primjer za broje 36416,
# funkcija vraća 3.

def djeljivo(broj):
    if broj == 0:
        return 0
    if (broj % 10) % 3 == 0:
        return 1 + djeljivo(broj // 10)
    return djeljivo(broj // 10)

print(djeljivo(36416))
