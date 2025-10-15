import random

count = 0  

while count < 10:
    broj = random.randint(0, 1000)  

    if 100 < broj < 500:
        print(broj)
        count += 1  

print("Ispisano je 10 brojeva")
