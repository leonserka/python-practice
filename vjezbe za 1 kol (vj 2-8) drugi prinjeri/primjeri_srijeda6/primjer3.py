
# Napisati program koji ispisuje sve brojeve od 10 do 100. Za svaki broj koji
# koji ima jednake znamenke, program ispisuje "buzz" umjesto broja.

for i in range(10, 100):
    if i // 10 == i % 10:
        print("buzz")
    else:
        print(i)