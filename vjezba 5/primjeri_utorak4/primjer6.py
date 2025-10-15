
# N.p. koji cita broj od korisnika i ispisuje
# koliko bitova broja je postavljeno na 1.

broj = int(input("broj: "))

cnt = 0
m = 1
while m <= broj:
    if (broj & m) == m:
        cnt += 1
    m = m << 1

print(cnt)