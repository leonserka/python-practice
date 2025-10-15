
# Napisati program koji zvjezdicama ispisuje dva kvadrata.
# Kvadrati su postavljeni dijagonalno (dolje-desno i gore-lijevo).
# Dužinu stranice kvadrata zadaje korisnik.

n = 5

# *****
# *****
# *****
# *****
# *****
# .....*****
# .....*****
# .....*****
# .....*****
# .....*****

for y in range(n*2):
    for x in range(n*2):
        if (y < n and x < n) or (y >= n and x >= n):
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
        