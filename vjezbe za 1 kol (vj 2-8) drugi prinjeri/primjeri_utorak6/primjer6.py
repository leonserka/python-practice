
# Napisati rekurzivnu funkciju koja prima dva broja i vraća
# koliko se znamenki brojeva razlikuju. Na primjer za brojeve
# 36415 i 32816, funkcija vraća 3.

# 00415
# 13415

def razlicite_znamenke(a, b):
    cnt = 0
    while a > 0 and b > 0:
        if a % 10 != b % 10:
            cnt += 1
        a //= 10
        b //= 10
    return cnt

def razlicite_rek(a, b):
    if a == 0 and b == 0:
        return 0
    if a % 10 != b % 10:
        return 1 + razlicite_rek(a // 10, b // 10)
    else:
        return 0 + razlicite_rek(a // 10, b // 10)

def razlicite_rek_tail(a, b, cnt=0):
    if a == 0 and b == 0:
        return cnt
    if a % 10 != b % 10:
        return razlicite_rek_tail(a // 10, b // 10, cnt+1)
    else:
        return razlicite_rek_tail(a // 10, b // 10, cnt+0)


print(razlicite_rek(415, 13415))
