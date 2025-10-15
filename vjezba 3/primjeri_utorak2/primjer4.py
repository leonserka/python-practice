
# ispisati svaku znamenku posebno

broj = int(input("cetveroznam broj"))

# 1234

z4 = broj % 10
broj = broj // 10
z3 = broj % 10
broj = broj // 10
z2 = broj % 10
broj = broj // 10
z1 = broj % 10
broj = broj // 10

print(z1, z2, z3, z4)