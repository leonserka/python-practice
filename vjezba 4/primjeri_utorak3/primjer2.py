
# Korisnik unosi brojeve dva po dva dok god ne unese
# drugi broj različit od 0. Nakon toga program ispisuje
# prvi broj podijeljen sa drugim.

a = int(input("prvi broj"))
b = int(input("prvi broj"))
while b == 0:
    a = int(input("prvi broj"))
    b = int(input("prvi broj"))

'''
b = 0
while b == 0:
    a = int(input("prvi broj"))
    b = int(input("prvi broj"))
'''
'''
while True:
    a = int(input("prvi broj"))
    b = int(input("prvi broj"))
    if b != 0:
        break
'''
'''
while b == 0:
    a = int(input("prvi broj"))
    b = int(input("prvi broj"))
'''
print(a/b)

