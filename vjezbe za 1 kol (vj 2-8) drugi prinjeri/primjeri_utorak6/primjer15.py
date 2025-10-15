
# 3. Napisati funkciju koja generira i ispisuje N slučajnih brojeva
# između 1 i 100, djeljivih sa 5. Funkcija dobiva N kao parametar.

from random import randint


def ispisi(n):
    cnt = 0
    while cnt < n:
        x = randint(1, 100)
        if x % 5 == 0:
            print(x)
            cnt += 1
        
ispisi(3)    