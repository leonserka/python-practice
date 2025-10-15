
# Ispisati slovo Z

# * * * *
#     *
#   *
# * * * *

n = int(input("n:"))

# gornja crta
for i in range(n):
    print("*", end=" ")
print()

# obrnuta dijagonala
#brr = n - 2
for y in range(n-2):
    for x in range(n-2-y):
        print(".", end=" ")
    print("*")
    #brr -= 1


# donja crta
for i in range(n):
    print("*", end=" ")
