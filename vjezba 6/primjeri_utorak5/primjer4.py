
# N.p. koji iscrtava prazan trokut na L

# *
# * *
# *   *
# *     *
# * * * * *

n = 15
for y in range(n):
    for x in range(n):
        if x == 0 or y == n-1 or x == y:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
