# 1) biringi juft toqligini topasiz. 2) ikkinchi toq bo'lsa 4 ga ko'pyatirb qaytarasiz
# juft bo'lsa ikkiga ko'paytirb qaytarasiz.
# 3) umumiy masala degan f-ya bu qolgan ikkisini chaqiradi
def jufttoq(n):
    if n % 2 == 0:
        return 0
    else:
        return 1
def amal(n, key):
    if key == 0:
        return n * 2
    else:
        return n * 4
def masala(n):
    k = jufttoq(n)
    return amal(n, k)
print(masala(2))