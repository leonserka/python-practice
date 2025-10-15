
# Prijestupna godina
# je godina koja je djeljiva sa 4, ali
# ne i sa 100 ili godina koja 
# je djeljiva sa 400

god = int(input("godina: "))

if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
    print("prijestupna")
else:
    print("nije prijestupna")
    