
# Napisati rekurzivnu funkciju koja vraća zbroj svih znamenaka
# broja.


def zbroji(broj):
    if broj == 0:
        return 0
    return (broj % 10) + zbroji(broj // 10)

print(zbroji(1234))