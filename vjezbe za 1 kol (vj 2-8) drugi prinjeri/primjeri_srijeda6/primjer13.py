

# Napisati rekurzivnu funkciju koja broji koliko je bitova nekog
# broja postavljeno na 1.

def prebroji(broj):
    cnt = 0
    while broj > 0:
        if broj & 1 == 1:
            cnt += 1
        broj = broj >> 1
    return cnt

def prebroji_rek(broj):
    if broj == 0:
        return 0
    if broj & 1 == 1:
        return 1 + prebroji_rek(broj >> 1)
    else:
        return 0 + prebroji_rek(broj >> 1)

def prebroji_rek2(broj, cnt=0):
    if broj == 0:
        return cnt
    if broj & 1 == 1:
        return prebroji_rek2(broj >> 1, cnt+1)
    else:
        return prebroji_rek2(broj >> 1, cnt+0)
    
print(prebroji_rek2(123))