
# Fizz-buzz
# Napisati program koji ispisuje
# sve brojeve od 1 do 1000, ali
# ako je broj djeljiv sa 3 ispisuje "fizz"
# ako je broj djeljiv sa 5 ispisuje "buzz"
# ako je broj djeljiv sa 3 i 5 ispisuje "fizz-buzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz-buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
        

