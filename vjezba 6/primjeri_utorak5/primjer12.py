from random import randint
import time
# ------K1------
# ---------K2---
# ----K3--------

duzina_trake = 30

def ispisi_traku(ime, poz):
    for i in range(duzina_trake):
        if i == poz:
            print(ime, end=" ")
        else:
            print("-", end=" ")
    print()

k1, k2, k3 = 0, 0, 0
while True:
    # iscrtati trake
    ispisi_traku("k1", k1)
    ispisi_traku("k2", k2)
    ispisi_traku("k3", k3)
    print()
    # pomaknuti konje
    k1 += randint(1, 3)
    k2 += randint(1, 3)
    k3 += randint(1, 3)
    # provjeriti kraj
    if k1 >= duzina_trake:
        break
    if k2 >= duzina_trake:
        break
    if k3 >= duzina_trake:
        break
    time.sleep(0.3)

print("rezultat:")
ispisi_traku("k1", k1)
ispisi_traku("k2", k2)
ispisi_traku("k3", k3)
print()
        