def djelitelj(broj,djelitelj):
    return broj%djelitelj==0
   
def brdjel(a):
    brojac=0
    for i in range(a,0,-1):
       if djelitelj(a,i):
           brojac+=1
           print(i, end=" ")
    print()
    return brojac
    
x = int(input("Unesite pozitivan broj: "))
while brdjel(x)<3:
    x = int(input("Unesite novi broj: "))
