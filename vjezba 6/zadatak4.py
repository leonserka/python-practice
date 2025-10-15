
def znamenka_funkcija(a,b):
    for i in range(b):
        znamenka=a%10
        a=a//10
    return znamenka

broj=int(input("Unesite broj: "))
n=int(input("Unesite mjesto znamenke: "))
while(n==0):
   n=int(input("Unesite broj koji nije 0 za mjesto znamenke: "))
   
if broj<0 or n<0:
    broj=abs(broj)
    n=abs(n)
    
print("Znamenka je: ", znamenka_funkcija(broj,n))
        

