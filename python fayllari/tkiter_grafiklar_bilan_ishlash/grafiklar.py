"""GUI -> grafik foydalanuvchilar"""
# # 1-misol
"""#1-usul
import tkinter
m=tkinter.Tk()
#vidjetlar bu yerda
m.mainloop()"""
#2-usul
"""from tkinter import *
m=Tk() #bu biz yaratgan oyna
#vidjetlar bu yerda
mening_labelim=Label(m, text="Assalomu Alaykum")
#oynaga joylash
mening_labelim.pack()
#m.mainloop() #oynani ushlab turish"""

#2-misol Button (tugma)
"""from tkinter import *
asosiy_oyna=Tk() #bu biz yaratgan oyna
asosiy_oyna.geometry("200x200")
#tugma qo'shish
#Button (oyna,text="matn", bd="qalinligi" command="oynani yopish")
tugma=Button(asosiy_oyna,text="Tanlang", bd="10")
tugma2=Button(asosiy_oyna,text="yopish", bd="10", command=asosiy_oyna.destroy)
tugma.pack()
tugma2.pack()
asosiy_oyna.mainloop() #oynani ushlab turish"""

#3-misol Button (tugma) stil qo'shish
"""from tkinter import *
asosiy_oyna=Tk() #bu biz yaratgan oyna
# asosiy oynaga olcham berish
asosiy_oyna.geometry("400x400")
v=StringVar(asosiy_oyna,'1')
qiymatlar={
    'Radiobutton 1':"1",
    'Radiobutton 2':"1",
    'Radiobutton 3':"1",
    'Radiobutton 4':"1",
    'Radiobutton 5':"1"
}
for (matn, qiymat) in qiymatlar.items():
    # radio button qurish:
    tugma = Radiobutton(
        asosiy_oyna,
        text=matn,
        variable=v,
        value=qiymat,
        indicator=0,
        background="blue"
    )
tugma.pack(ipadx=100,ipady=200)
#asosiy oynani ushlab turish
asosiy_oyna.mainloop()"""

# # 4 - misol
# # radio button
"""from tkinter import *

# asosiy oynani yasash
asosiyOyna = Tk()

# o'lcham berish
asosiyOyna.geometry('400x400')

# string ma'lumotlardan foydalanish uchun
# bu yerda birinchi radio button tanlanib turadi
v = StringVar(asosiyOyna, '1')

# tugmalar qiymatlarini saqlash uchun lig'at
qiymatlar = {
    'RadioButton 1': "1",
    'RadioButton 2': "2",
    'RadioButton 3': "3",
    'RadioButton 4': "4",
    'RadioButton 5': "5"
}

# barcha tugamalarni Asosiy oynaga joylash uchun for loop
for (matn, qiymat) in qiymatlar.items():
    # radio button qurish:
    tugma = Radiobutton(
        asosiyOyna,
        text=matn,
        variable=v,
        value=qiymat,
        background="white"
    )
    #     pack(x kordinata, y kordinata)
    tugma.pack(side=TOP, ipady=5)

# oynani ushlab turish uchun
asosiyOyna.mainloop()"""

# 5 - misol checkBox
"""from tkinter import *

# oynani qurish
asosiy_oyna = Tk()

# oynaga o'lcham
asosiy_oyna.geometry('300x400')
# label qurish
w = Label(asosiy_oyna, text="Checkbox lar", font='50')

# labelni joylash
w.pack()

# # checkboxlarni int qiymat qabul qiladigan qilib e'lon qilsih
# Checkbutton1 = IntVar()
# Checkbutton2 = IntVar()
# Checkbutton3 = IntVar()

button1 = Checkbutton(asosiy_oyna, text="qora",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button2 = Checkbutton(asosiy_oyna, text="yashil",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button3 = Checkbutton(asosiy_oyna, text="qizil",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0,
                      height=5,
                      width=10)

button1.pack()
button2.pack()
button3.pack()

asosiy_oyna.mainloop()"""

# 6 - misol Canvas
"""# oddiy shakl yaratish
from tkinter import *

asosiy_oyna = Tk()

# canvas yaratish
C = Canvas(
    asosiy_oyna,  # asosiy oynada
    bg="yellow",  # fon rangi
    height=500,  # balandligi
    width=800  # eni
)

# chiziq yaratish
chiziq = C.create_line(100, 120, 320, 40, fill="green", width=5)

# burchak yaratish
burchak = C.create_arc(180, 150, 80, 210, start=0, extent=180, fill="red")

# oval yaratish
oval = C.create_oval(80, 30, 140, 150, fill="blue")

# canvasni asosiy oynaga joylash
C.pack()
asosiy_oyna.mainloop()"""

# 7- misol Chizadigan ilova convas yordamida:
# oddiy shakl yaratish
from tkinter import *

asosiy_oyna = Tk()

# Sarlovha

