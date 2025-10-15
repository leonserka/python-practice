

def f1(a):
    a = 2 * a

def f2(a):
    b = 2 * a
    return b

def f3(a):
    return 2 * a

for i in range(3):
    print(f1(i))
    x = 1 + 2*i
    f2(x)
    print(x)
    y = 2 * f3(i)
    print(f3(y))

    

    