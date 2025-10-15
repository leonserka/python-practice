
def prost(broj):
    if broj == 1:
        return False
    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True

broj = int(input("broj: "))
if prost(broj):   
    print("prost")
else:
    print("nije prost")    