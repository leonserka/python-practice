#a)  x+2 (x-2)
x=int(input("unesi x:"))

z=x+2*(x-2)
print("z=",z)


#b) (x+2)(x-2)
x=int(input("unesi x:"))

z1=(x+2)*(x-2)
print("z1=",z1)


#c) +(x+2) x
x=int(input("unesi x:"))

z2=(x+2)*x
print("z2=",z2)


#d) x+2 Or x == 2
x=int(input("unesi x:"))

z3= x+2 or x == 2
print("z3=",z3)


#e) x <= 2 and x => 2
x=int(input("unesi x:"))

z4= x <= 2 and x >=2
print("z4=",z4)


#f) x = 2 and x >= 2
x=int(input("unesi x:"))

z5=x == 2 and x >= 2
print("z5=",z5)


#g) x = 2 == x and x =! 2
x=int(input("unesi x:"))

z6= x == 2 == x and x != 2
print("z6=",z6)