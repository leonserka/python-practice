#a) jesu li a i b pozitivni
a=int(input("unesi a="))
b=int(input("unesi b="))

if  a>0  and b >0:
   print("pozitivni")
else :
     print("negativni")  
     
          
#b) jesu li a ili b parni    
a=int(input("unesi a="))
b=int(input("unesi b="))

if  a % 2 == 0  and b % 2 == 0:
   print("parni")
else :
     print("neparni")  
     
         
#c) jesu li a i b parni, a a veće od b
a=int(input("unesi a="))
b=int(input("unesi b="))
flag = False
if a >b :
    flag = True
    print(" a je veci od b")
if b > a:
    flag = True
    print("b je veci od a")
    

if a % 2 == 0 and b % 2 == 0 :
    print("parni")
else:
    print("neparni")   
    
       
#d je li barem jedan od a i b neparan
a=int(input("unesi a="))
b=int(input("unesi b="))

if  a % 2 != 0  or b % 2 != 0:
   print("barem jedan je neparan")
else :
     print("oba su parna")  
     
#e) je li najviše jedan od a i b neparan
a=int(input("unesi a="))
b=int(input("unesi b="))

if  a % 2 != 0  and b % 2 == 0:
      print("samo  je a neparan")    
elif  a % 2 == 0  and b % 2 != 0:
    print("samo  je b1 neparan")
else :
     print("oba su neparna ili nijedan")  

#f) je li a djeljiv sa b ili obrnuto

a=int(input("unesi a="))
b=int(input("unesi b="))

if  a % b == 0  or b % a == 0:
      print(" a je djeljiv sa b ili obrnuto ")    
else :
     print("a nije djeljiv sa b ili obrnuto ") 
     
     
 #g) je li a djeljiv sa b, a b nije djeljiv sa a

a=int(input("unesi a="))
b=int(input("unesi b="))

if  a % b == 0 :
      print("a je djeljiv sa b") 
elif b%a!=0:
    print(" b nije djeljiv sa a")    
else :
     print("a nije djeljiv sa b") 
     
     
     
     
 