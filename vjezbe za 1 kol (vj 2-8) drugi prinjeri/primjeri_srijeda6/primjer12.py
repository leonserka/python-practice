

# Napisati program koji od korisnika čita brojeve. Ako uneseni
# broj ima manje od 3 djelitelja, program nastavlja sa čitanjem
# brojeva. U suprotnom program završava. Program se oslanja na
# dodatnu funkciju brdjel() koja prima broj i vraća broj djelitelja
# primljenog broja. Napisati funkciju brdjel()

def brdjel(broj):
    cnt = 0
    for d in range(1, broj+1):
        if broj % d == 0:
            cnt += 1
    return cnt

broj = int(input("broj: "))
while brdjel(broj) < 3:
    broj = int(input("broj: "))
    