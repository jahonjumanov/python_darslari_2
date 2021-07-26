# ism familiya kiritish bunda agar kiritgan satrda probel bo'lmasa qayta kiritsin
while True:
    name = input("ism: ")
    """grandFatherName = input("ism: ")
    fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    name = name.split()
    if len(name) == 1:
        break
    elif len(name) > 1:
        print("Faqat ism  kerak ortiqchani yozmang!")
    else:
        print("Ism  kiriting!")
str = " "
ism = (str.join(name))
while True:

    grandFatherName = input("Katta otasining ismi: ")
    """fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    grandFatherName = grandFatherName.split()
    if len(grandFatherName) == 1:
        break
    elif len(grandFatherName) > 1:
        print("Katta otasining ismi")
    else:
        print("Katta otasining ismi")
str = " "
kattaOta = (str.join(grandFatherName))
while True:

    FatherName = input("Otasining ismi: ")
    """fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    FatherName = FatherName.split()
    if len(FatherName) == 1:
        break
    elif len(FatherName) > 1:
        print("Katta otasining ismi")
    else:
        print("Katta otasining ismi")
str = " "
ota = (str.join(FatherName))
while True:

    jinsi = input("Jinsi: ")
    """fatherName = input("ism: ")
    jinsi = input("ism: ")"""
    jinsi = jinsi.split()
    asd = str.join(jinsi)
    jins = "Erkak"
    jins1 = "erkak"
    jin2 = "Ayol"
    jins3 = "Erkak"
    if asd == jins or asd==jins1 or asd == jin2 or asd == jins3 and len(FatherName) == 1:
        break

    elif len(jinsi) > 1:
        print("Jinsini kiriting")
    else:
        print("Jinsini kiriting")
str = " "
jins = (str.join(jinsi))

if jins == "erkak" or jins == "Erkak":
    print(kattaOta+"ov",ism,ota+"ovich")
else:
    print(kattaOta+"ova",ism,ota+"ovna")