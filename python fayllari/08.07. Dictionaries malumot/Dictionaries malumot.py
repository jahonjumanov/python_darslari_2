"""Dictionaries (lug'at)"""
# to'g'ridan to'g'ri qo'yish
shaxs = {
    "Ism": "Jahongir",
    "Yoshi": 27,
    "Kasbi": "o'qituvchi"
}
print(type(shaxs))

""" Dict (lug'at) """

# to'g'ridan to'g'ri e'lon qilish
shaxs = {
    "ism": "Oybek",
    "yoshi": 22,
    "kasbi": "O'qituvchi"
}

# dict() konstruktori bilan
shaxs = dict({"ism": "Oybek", "yoshi": 22, "kasbi": "O'qituvchi"})

print(type(shaxs))

""" dict xossalari """
# dict bu tartiblangan
# elementlar takrorlanmaydi
# element -> {key : value}
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "yoshi": 22,
    "kasbi": "O'qituvchi"
}
print(shaxs)

""" elementlarga murojaat """
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi"
}
# 1 - usul

print(shaxs["ism"])

# 2 usul get() metodi bilan

print(shaxs.get("ism"))

""" keys() metodi faqatgina kalit so'zlarni
    chiqarar ekan """
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi"
}

print(shaxs.keys())

""" values() nu metod faqatgina
    qiymatlarni chiqarar ekan """
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi"
}

print(shaxs.values())

""" element qo'shish """
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi"
}
# oddiy yangi elementni e'lon qilib:
shaxs["millati"] = "O'zbek"
print(shaxs)

# update() bir nechta elemnet qo'shishingiz mumkin
shaxs.update({"manzili": "Jizzax", "tel": "+99 894 646 24 99"})
print(shaxs)

""" element o'zgatirsh -> update"""
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi"
}
shaxs["ism"] = "Nodir"
print(shaxs)  # endi ismi Nodir bo'ldi

""" element o'chirish """
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

# pop() -> dict.pop(any key) # dict - lug'at; any - har (lyuboy) key - kalit
shaxs.pop("millati")
print(shaxs)

# popitem() -> bu dict ni oxirgi elementini o'chiradi # dict.popitem() no parameter
shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

shaxs.popitem()
print(shaxs)

# del -> del dict[key] - bunda o'sha key ga mos element o'chib ketadi
# del -> del dict  -  bu dict ni o'zini xotiradan o'chiradi

shaxs = {
    "ism": "Oybek",
    "yoshi": 20,
    "kasbi": "O'qituvchi",
    "millati": "O'zbek"
}

del shaxs["yoshi"]
print(shaxs)

del shaxs  # o'chib ketdi...
# print(shaxs)  agar buni kommentdan chiqarsan qib qizil xato bo'ladi