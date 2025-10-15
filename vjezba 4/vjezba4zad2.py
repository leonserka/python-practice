
a = 42  
b = 17 

# a) 
if a & 1:  
    print("a) Zadnji bit  je postavljen na 1")
else:
    print("a) Zadnji bit nije postavljen na 1")

# b) 
if (a >> 3) & 1:
    print("b) Četvrti bit je postavljen na 1")
else:
    print("b) Četvrti bit nije postavljen na 1")

# c) 
if (a & 7) == (b & 7): #7= 111
    print("c) Zadnja tri bita su jednaka")
else:
    print("c) Zadnja tri bita nisu jednaka")

# d) 
if ((a >> 1) & 7) == ((b >> 1) & 7):
    print("d) Predzadnja tri bita su jednaka")
else:
    print("d) Predzadnja tri bita nisu jednaka")

# e) 
if (a & (1 << 3))==8 and (a & (1 << 5))==32: #==8 jer 8=1000(1 je samo na 4 bitu)  , a 32=100000 ( 1 je samo na 6 bitu)
    print("e) Četvrti i šesti bit su postavljeni na 1")
else:
    print("e) Četvrti i/ili šesti bit nisu postavljeni na 1")

# f)
if (a & (1 << 3))==8 or (a & (1 << 5))==32:  
    print("f) Četvrti ili šesti bit su postavljeni na 1")
else:
    print("f) Ni četvrti ni šesti nisu postavljeni na 1")

# g) 
if ((a & (1 << 3))==8 and not (a & (1 << 5)))==32 or (not (a & (1 << 3))==8 and (a & (1 << 5)))==32:
    print("g) Samo četvrti ili šesti bi je postavljen na 1")
else:
    print("g) Niti četvrti niti šesti bit nije postavljeni na 1")



