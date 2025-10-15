
from random import randint

# Ajnc

# Igrac uzima karte jednu po jednu dok ne odluči stati ili izleti
zbroj_igrac = 0

while True:
    print("Trenutni zbroj karata igrača", zbroj_igrac)
    odgovor = input("Još jedna karta?")
    if odgovor == "ne":
        break
    karta = randint(1, 10)
    zbroj_igrac += karta
    if zbroj_igrac > 21:
        print("Igrač izletio")
        break
print("Konačni zbroj igrača", zbroj_igrac)

# Kuca uzima karte dok ne sustigne igraca
zbroj_kuca = 0
if zbroj_igrac <= 21:
    while zbroj_kuca < zbroj_igrac:
        print("Trenutni zbroj karata kuće", zbroj_kuca)
        karta = randint(1, 10)
        zbroj_kuca += karta
        if zbroj_kuca > 21:
            break

print("Konačni zbroj kuće", zbroj_kuca)

# Dobitak: kuca dobiva sve nerijeseno, tko je izletio ili veci zbroj
if zbroj_igrac > 21:
    print("Kuća dobiva 1")
elif zbroj_kuca > 21:
    print("Igrač dobiva 1")    
elif zbroj_igrac > zbroj_kuca:
    print("Igrač dobiva 2")
elif zbroj_igrac <= zbroj_kuca:
    print("Kuća dobiva 2")
    









