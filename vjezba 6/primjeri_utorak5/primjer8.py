
# ispisati znamenke broja u obrnutom i pravom redoslijedu

# 1234

def ispisi(broj):
    while broj > 0:
        print(broj % 10)
        broj = broj // 10

def ispisi_rek(broj):
    if broj == 0:
        return
    print(broj % 10)
    ispisi_rek(broj // 10)

def ispisi_rek_isp(broj):
    if broj == 0:
        return
    ispisi_rek_isp(broj // 10)
    print(broj % 10)

ispisi_rek_isp(1234)