# a)
x = 5
y = 3
z=(x / 2) + (y / 2) # očekuje se 4
print(z)




#b)
# x = 5
# y = x + 5
# x + y % 2

x=5
y=x+5
z=(x+y)%2
print("z=",z)
#potrebno je staviti zagrade jer inace program prvo rjesaje y%2  a ne x+y kako je potrebno


#c)

#x = 1234
# očekuje se ispisi: 1, 2, 3 i 4  
x=1234
z4 = x % 10
z3 = (x % 100)//10
z2 =( x % 1000)//100
z1 = x //1000
print(z1, z2, z3, z4)