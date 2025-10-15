
# N.p. koji iscrtava prazan trokut na L

# *

# * *
# *   *
# *     *

# * * * * *

def linija(brr):
    print("*", end=" ")
    for i in range(brr):
        print(".", end=" ")
    print("*")

n = 15
print("*")

for i in range(n-2):
    linija(i)

for i in range(n):
    print("*", end=" ")
