
# N.p. koji cita broj od korisnika i ispisuje
# da li se unutar bitova broja nalazi pattern "1011".

broj = int(input("broj: "))

p = 11 # 1011
m = 15 # 1111
while p <= broj:
    if (broj & m) == p:
        print("da")
    m = m << 1
    p = p << 1


'''
p = 11 # 1011
m = 15 # 1111
while broj > 0:
    if (broj & m) == p:
        print("da")
    broj = broj >> 1
'''

