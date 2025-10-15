
# Napisati program koji od korisnika čita brojeve. Program čita
# brojeve dok god su upisani brojevi naizmjenice parni i neparni

pa = int(input("broj: "))
a = int(input("broj: "))
while pa % 2 != a % 2:
    pa = a
    a = int(input("broj: "))
    
    