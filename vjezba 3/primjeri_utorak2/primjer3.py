
# iz troznamenkastog broja ispisati
# svaku znamenku posebno

broj = int(input("troznamenkasti broj"))

# 123
z1 = broj // 100
#z2 = (broj // 10) % 10
z2 = (broj % 100) // 10 
z3 = broj % 10

print(z1, z2, z3)