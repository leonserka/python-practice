
# Napisati program koji od korisnika čita dva po dva broja, 
# ukupno 20 brojeva. Svaka dva broja predstavljaju rezultat 
# nekog natjecanja i oba broja moraju biti pozitivna, a zbroj
# im mora biti 100. Ako uneseni brojevi nisu ispravni, 
# program ispisuje grešku i traži ponovan unos. 
# Na kraju program ispisuje prosjek prvih i 
# prosjek drugih brojeva.

cnt = 0
suma, sumb = 0, 0
while cnt < 10:
    a = int(input("a: "))
    b = int(input("b: "))
    if a > 0 and b > 0 and a+b == 100:
        cnt += 1
        suma += a
        sumb += b
    else:
        print("greška")

print(suma / 10, sumb / 10)
        