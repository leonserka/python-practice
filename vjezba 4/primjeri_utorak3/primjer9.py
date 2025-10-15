
# Korisnik unese broj, program ispise
# svaku znamenku broja odvojeno.

broj = int(input("broj: "))

while broj > 0:
    z = broj % 10
    broj = broj // 10
    print(z)