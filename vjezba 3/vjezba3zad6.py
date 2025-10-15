a=int(input("unesi a="))
b=int(input("unesi b="))
c=int(input("unesi c="))



if a>b and b>c:
    print(a,b,c)
elif a>b and c>b and a>c:
    print(a,c,b)
elif a<b and c<b and a<c:
    print(b,c,a)  
elif a<b and c<b and a>c:
    print(b,a,c)   
elif a>b and c>b and a<c:
    print(c,a,b)  
else:
    print(c,b,a)     
        