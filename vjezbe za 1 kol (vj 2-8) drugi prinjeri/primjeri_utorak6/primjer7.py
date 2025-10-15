
# Napisati program koji od korisnika čita (neparnu) visinu slova i
# zvjezdicama ispisuje slovo N.

n = int(input("n: "))

# *   *

# **  *
# * * *
# *  **

# *   *

for y in range(n):
    for x in range(n):
        if x == y or x == 0 or x == n-1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
        