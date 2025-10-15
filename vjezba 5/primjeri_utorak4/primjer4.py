
# Napisati program koji za broj ispise sve njegove djeljitelje.

broj = int(input("broj: "))
for i in range(1, broj+1):
    if broj % i == 0:
        print(i)
