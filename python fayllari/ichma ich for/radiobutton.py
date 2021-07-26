# radio button
from tkinter import *

# asosiy oynani yasash
asosiyOyna = Tk()

# o'lcham berish
asosiyOyna.geometry('150x150')

# string ma'lumotlardan foydalanish uchun
v = StringVar(asosiyOyna, '1')

# tugmalar qiymatlarini saqlash uchun lig'at
qiymatlar = {
    'Erkak': "1",
    'Ayol': "2",
}
# barcha tugamalarni Asosiy oynaga joylash uchun for loop
for (matn, qiymat) in qiymatlar.items():
    # radio button qurish:
    tugma = Radiobutton(
        asosiyOyna,
        text=matn,
        variable=v,
        value=qiymat,
        indicator=0,
        background="blue"
    )
    #     pack(x kordinata, y kordinata)
    tugma.pack(side=TOP, ipady=5)

# oynani ushlab turish uchun
asosiyOyna.mainloop()