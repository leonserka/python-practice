
# 3. Napisati program koji u petlji ispisuje proste brojeve od 1 do
# 1000. Program se oslanja na funkciju prost() koja provjerava da
# li je broj prost (vraća True ili False, napisati funkciju).

def prost(broj):
    if broj == 1:
        return False
    for d in range(2, broj):
        if broj % d == 0:
            return False
    return True

for i in range(1, 1001):
    if prost(i):
        print(i)
