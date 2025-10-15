
# N... gdje ce korisnik unjeti broj, a program ispisati
# da li je broj prost.

broj = int(input("broj: "))

brd = 0
for i in range(1, broj+1):
    if broj % i == 0:
        brd += 1

if brd <= 2:   
    print("prost")
else:
    print("nije prost")


'''
prost = True
for i in range(2, broj):
    if broj % i == 0:
        prost = False
        break

if prost:   
    print("prost")
else:
    print("nije prost")
'''