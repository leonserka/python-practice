sum=0
x=int(input("Unesite broj: "))

while x<0:
    x=int(input("Unesite ne-negativan broj: "))
    
while(x>0):
    if x & 1==1:
        
        y=int(input("Unesite broj: "))
        sum+=y
    x=x >>1
    
print("Zbroj unesenih brojeva: ",sum)

