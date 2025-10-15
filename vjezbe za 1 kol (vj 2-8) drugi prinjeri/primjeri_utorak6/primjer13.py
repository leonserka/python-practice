
# Napisati funkciju koja prima broj kao parametar i ispisuje
# zvjezdice i razmake u jednom redu. Funkcija za svaki bit broja
# postavljena na 1 ispisuje zvjezdicu, a za svaki bit postavljen 
# na 0 ispisuje razmak.

def ispisi(broj):
    while broj > 0:
        if broj & 1 == 1:
            print("*", end=" ")
        else:
            print(".", end=" ")
        broj = broj >> 1

def ispisi_rek(broj):
    if broj == 0:
        return
    if broj & 1 == 1:
        print("*", end=" ")
    else:
        print(".", end=" ")
    ispisi_rek(broj >> 1)

ispisi_rek(123)