parni = 0
neparni = 0

for i in range(10):
    a = int(input("Unesite broj: "))
    
    # Ignoriraj nule
    if a == 0:
        continue
    
    if a % 2 == 0:
        parni += 1
    else:
        neparni += 1

print(f"Brojeva parnih: {parni}")
print(f"Brojeva neparnih: {neparni}")