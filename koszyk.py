koszyk = [{'produkt': 'talerz', 'ilosc': 6, 'cena': 2.5},
 {'produkt': 'cukiernica', 'ilosc': 1, 'cena': 5},
 {'produkt': 'dzbanek', 'ilosc': 2, 'cena': 7}]

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
