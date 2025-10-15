
# Napisati program koji od korisnika čita brojeve. Program čita
# brojeve dok god je svaki upisani broj djeljiv sa prethodno upisanim
# brojem.

pa = 1
a = int(input("a: "))
while a % pa == 0:
    pa = a
    a = int(input("a: "))

        
    