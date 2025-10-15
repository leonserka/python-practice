
# Napisati funkciju koja čita dva po dva broja dok god korisnik ne
# unese dva broja koja su oba veća od prethodna dva broja.
# Funkcija nakon toga vraća ta dva broja. Prva dva unesena broja
# se ne vraćaju.

def procitaj():
    pa = int(input("a:"))
    pb = int(input("b:"))
    while True:
        a = int(input("a:"))
        b = int(input("b:"))
        if a > pa and b > pb:
            return a, b
        pa = a
        pb = b
    
        


print(procitaj())