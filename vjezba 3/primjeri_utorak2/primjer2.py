# Korisnik upiše ukupan broj sekundi, a
# program ispisuje sate, minute i sekunde

# 59253

ukupno = int(input("Ukupan broj sekundi"))

sati = ukupno // 3600
minute = (ukupno // 60) % 60
sekunde = ukupno % 60

print(sati, minute, sekunde)

