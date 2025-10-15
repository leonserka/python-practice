broj = 0
while True:
    a = int(input("Unesite broj : "))
    
    if a == 0:
        break
    elif a < 0:
        broj += 1
        while a < 0:
            a = int(input("Unesite pozitivan broj: "))

print(f"Broj pogrešnih  unosa: {broj}")