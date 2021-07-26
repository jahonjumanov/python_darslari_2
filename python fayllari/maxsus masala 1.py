# maxsus masala 1

# ism familiya kiritish bunda agar kiritgan satrda probel bo'lmasa qayta kiritsin
while True:
    fullName = input("ism familiya kiriting: ")  # Oybek Narzullayev
    fNameArray = fullName.split()
    if len(fNameArray) == 2:
        break
    elif len(fNameArray) > 2:
        print("Faqat ism familiya kerak ortiqchani yozmang!")
    else:
        print("Ism va familiyani kiriting!")

while True:
    age = input("Yoshingizni kiriting: ")
    if int(age) >= 18:
        break
    else:
        print("18 yoshdan katta bo'lsin")