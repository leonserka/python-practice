
# 1. Napisati program koji od korisnika čita 10 
# pozitivnih brojeva. Nakon svakog unosa, program ispisuje 
# sve djelitelje unesenog broja. Program ignorira negativne 
# brojeve. Ako korisnik unese 0,
# program ispisuje "kraj" i prekida se.

def ispisi_djelitelje(broj):
    for i in range(1, broj+1):
        if broj % i == 0:
            print(i)

n = 0
while n < 10:
    broj = int(input("broj: "))
    if broj > 0:
        n += 1
        ispisi_djelitelje(broj)
    elif broj == 0:
        print("kraj")
        break
        
        