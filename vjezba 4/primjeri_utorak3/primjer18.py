
# Ispisati slovo T

# * * *

#   *
#   *

n = int(input("n:"))

for i in range(n):
    print("*", end=" ")

print()

for j in range(n-1):
    for i in range(n // 2):
        print(".", end=" ")
    print("*")
