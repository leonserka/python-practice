
# V

# *      *
#  *    *
#   *  *
#    **

n = 10
for y in range(n):
    for x in range(2*n):
        if x == y or x == 2*n-y-1:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()