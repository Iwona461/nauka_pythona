password = "secret"

dlugosc_srodka = len(password) - 2
srodek = '*' * dlugosc_srodka

print(password[0] + srodek + password[-1])
