
def zamijeni(a, b):
    return b, a

a = 6
b = 3
print(a, b)
a, b = zamijeni(a, b)
print(a, b)


'''
# ne radi
def zamijeni(a, b):
    a, b = b, a

a = 6
b = 3
print(a, b)
zamijeni(a, b)
print(a, b)
'''