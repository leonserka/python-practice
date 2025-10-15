
# Napisati rekurzivnu funkciju "djelitelji" koja ispisuje sve
# djelitelje broja 333.

def djelitelji():
    for d in range(1, 334):
        if 333 % d == 0:
            print(d)

def djelitelji_rek(d=1):
    if d > 333:
        return
    if 333 % d == 0:
        print(d)
    djelitelji_rek(d+1)
        
            
djelitelji_rek()
    