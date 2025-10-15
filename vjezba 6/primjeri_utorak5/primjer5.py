
# 0..4

def zbroj_do_n(n):
    # temeljni 
    if n == 0:
        return 0
    # rekurzivni
    return zbroj_do_n(n-1) + n

print(zbroj_do_n(3))
'''
def zbroj_do_0():
    return 0

def zbroj_do_1():
    return zbroj_do_0() + 1

def zbroj_do_2():
    return zbroj_do_1() + 2

def zbroj_do_3():
    return zbroj_do_2() + 3

def zbroj_do_4():
    return zbroj_do_3() + 4

zbroj_do_3()

'''
'''
def zbroj_do_0():
    return 0

def zbroj_do_1():
    return 0 + 1

def zbroj_do_2():
    return 0 + 1 + 2

def zbroj_do_3():
    return 0 + 1 + 2 + 3

def zbroj_do_4():
    return 0 + 1 + 2 + 3 + 4
'''