
# Pi

from random import randint

n = 10000
a = 1000

c = 0
for i in range(n):
    x = randint(-a, a)
    y = randint(-a, a)
    if x**2 + y**2 < a**2:
        c += 1

print(4 * c / n)    