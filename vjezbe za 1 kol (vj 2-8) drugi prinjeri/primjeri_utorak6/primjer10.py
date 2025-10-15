
# *****
# *   *
# *   *
# *   *
# *****
# **
# * *
# *  *
# *   *

n = 6
for y in range(2*n):
    for x in range(n):
        if x == 0 or y == 0 or y == n-1 or (x == n-1 and y < n):
            print("*", end=" ")
        elif x == y-n and y > n:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()