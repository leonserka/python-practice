
def srednjiBroj(a, b, c):
   if a > b:
       a, b = b, a
   if b > c:
       b, c = c, b
   if a > b:
       a, b = b, a
   return b

a=int(input("Unesite prvi broj: "))
b=int(input("Unesite drugi broj: "))
c=int(input("Unesite treci broj: "))

print("Srednji broj je: ",srednjiBroj(a,b,c))

