
# Napisati funkciju koja ispisuje određeni broj
# razmaka i određeni broj zvjezdica u jednom redu.

# ....***
def ispisi(brr, brz):
    for i in range(brr):
        print(".", end=" ")
    for i in range(brz):
        print("*", end=" ")
    print()

n = 10
for i in range(n):
    ispisi(n-1-i, i+1)

#n = 10
#for i in range(n):
#    ispisi(i+1, 0)

'''
dva kvadrata
n = 10
for i in range(n // 2):
    ispisi(0, n // 2)
    
for i in range(n // 2):
    ispisi(n // 2, n // 2)
'''
    
    