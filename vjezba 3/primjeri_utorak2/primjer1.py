
# Korisnik upiše sate, minute i sekunde, a
# program ispisuje ukupan broj sekundi.

# unos
sati = int(input("unesite sate:"))
minute = int(input("unesite minute:")) 
sekunde = int(input("unesite sekunde:"))

# izracun
ukupno = sati * 3600 + minute * 60 + sekunde

# ispis
print("Ukupan broj sekundi je", ukupno)