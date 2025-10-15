# Napisati program koji od korisnika čita N i ispisuje sve brojeve
# do N koji završavaju sa 321.

n = 10000

for i in range(n+1):
    if i % 1000 == 321:
        print(i)