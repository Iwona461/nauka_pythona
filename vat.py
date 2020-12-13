def calucate_vat(netto):
    return (netto * 23)/100

if __name__ == "__main__":
    vat = calucate_vat(777)
    print("{0}". format(vat))
