
# Napisati rekurzivnu funkciju koja ispisuje zadani broj zvjezdica.

def ispisi(brz):
    if brz == 0:
        return
    print("*")
    ispisi(brz-1)

ispisi(10)