
def ispisi_do_0():
    print(0)

def ispisi_do_1():
    ispisi_do_0()
    print(1)

def ispisi_do_2():
    ispisi_do_1()
    print(2)

def ispisi_do_3():
    ispisi_do_2()
    print(3)

def ispisi_do_n(n):
    if n == 0:
        print(0)
        return
    print(n)
    ispisi_do_n(n-1)

ispisi_do_3()
ispisi_do_n(5)
