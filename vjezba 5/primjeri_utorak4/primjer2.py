
j = 0
n = 4
while j < n:
    if j % 2 == 0:
        j += 1
    else:
        j *= 2
    print(j)
    for i in range(j, 0):
        print(i)