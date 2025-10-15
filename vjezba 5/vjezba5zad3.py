broj = int(input("Unesite cijeli broj: "))  
brojac=0
n=0
while(n<32):
    if broj & (2**n)!=0:
        brojac+=1
      
    n+=1
print("Broj jedinica: ", brojac)




#7=111(rj=3)
#3=011(rj=2)
