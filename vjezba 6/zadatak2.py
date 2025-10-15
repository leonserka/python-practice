
n=int(input("Unesite broj: "))
while(n<0):# negativan broj == ponavljanje
    n=int(input("Unesite pozitivan broj: "))
if(n%2==0): #ako se da paran broj +1 
    n+=1
    
for y in range(n): #vertikalno
    for x in range(n): #horizontalno
        if x == 0 or x == n - 1 or y == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()






#b)
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