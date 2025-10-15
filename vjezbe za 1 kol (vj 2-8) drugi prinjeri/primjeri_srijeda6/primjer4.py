
# 2. Napisati program koji od korisnika čita (neparnu) visinu slova i zvjezdicama
# ispisuje broj 8 (kao na digitronu).

n = int(input("n: "))

# ****
# *  *
# *  *
# ****
# *  *
# *  *
# ****

for y in range(n):
    for x in range(n//2):
        if x == n//2-1 or x == 0 or y == 0 or y == n-1 or y == n // 2:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()
        