koszyk = [{'produkt': 'twix', 'ilosc': 3, 'alergeny' : 'czekolada, orzechy', 'cena': 2.5},
 {'produkt': 'mleko', 'ilosc': 1, 'alergeny' : ' laktoza', 'cena': 2},
 {'produkt': 'chleb', 'ilosc': 2, 'alergeny': 'gluten', 'cena': 7},
 {'produkt': 'sok', 'ilosc': 3, 'alergeny': '', 'cena': 4}]

suma = 0
for poz in koszyk:
    il = poz['ilosc']
    c = poz['cena']
    suma = suma + (c * il)
    print(poz)

    # print(c)
    # print(suma)
    # print(poz)
print(suma)

for poz in koszyk:
    al = poz['alergeny']
    p = poz['produkt']
    if al == "":
        print(p + ' jest zdrowym produktem')
