#ip adresa == 3292799233 (196.68.33.1)
#a  
ip = int(input("Unesite cijeli broj IP adrese: "))  


prvi_dio = (ip >> 24) & 255 #255 = bin(11111111)
drugi_dio = (ip >> 16) & 255

if prvi_dio == 196 and drugi_dio == 68:
    print("a) Prva dva dijela adrese su 196 i 68 ")
else:
    print("a) Prva dva dijela adrese nisu 196 i 68")


#b
ip = int(input("Unesite cijeli broj IP adrese: "))  


treci_dio = (ip >> 8) & 255
cetvrti_dio = ip & 255

if treci_dio < 128 and cetvrti_dio < 128:
    print("b) Zadnja dva dijela adrese su manji od 128")
else:
    print("b) Zadnja dva dijela adrese nisu manji od 128")


#c

ip = int(input("Unesite cijeli broj IP adrese: "))  


prvi_dio = (ip >> 24) & 255
cetvrti_dio = ip & 255

if prvi_dio == cetvrti_dio:
    print("c) Prvi i zadnji dio adrese su jednaki")
else:
    print("c) Prvi i zadnji dio adrese nisu jednaki")

#a)rjesavanje prvi dio 
#11000100  (ip >> 24mjesta u desno)
#11111111  (255 binarno)
#---------
#11000100   (dali je ip and 255 == 196 bin)