
# Korisnik unese broj, program ispise
# sve bitove broja odvojeno.

broj = int(input("broj: "))

while broj > 0:
    z = broj & 1
    broj = broj >> 1
    print(z)
'''
while broj > 0:
    z = broj % 2
    broj = broj // 2
    print(z)
'''