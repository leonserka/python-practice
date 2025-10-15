
# Ispisati slovo Z

# * * * *
#     *
#   *
# * * * *

n = int(input("n:"))

for y in range(n):
    for x in range(n):
        if y == 0 or y == n-1 or x == n - y - 1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
