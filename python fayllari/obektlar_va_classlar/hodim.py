# 1. dastlab xodimlar sonini kiriting.
# 2. har bir xodim ma'lumotlarini input qilib obyekt yarating
# 3. gap() metodida agar oyligini 1mln dan past bo'lsa
# "mening oyligim kam degan yozuv ham chiqsin"
# 4. barcha xodim ma'lumotlarini gap metodi orqali konsolga chiqaring
class Xodim:
    def __init__(self, Ismi,manzili,maoshi):
        self.Ismi = Ismi
        self.manzili = manzili
        self.maoshi = maoshi
    def maosh(self):
        print(f"Mening ismim {self.Ismi}, Maoshim {self.maoshi}")
        if self.maoshi<1000000:
            print("Mening maoshim kam")

xodimlar=[]
son=int(input("Xodimlar sonini kiriting:"))
for i in range(son):
    print(f"{i+1}-xodim")
    Ismi=input("Ism kiriting")
    manzili=input("Manzil kiriting")
    maoshi=input("Maoshini kiriting")
    xodimlar.append(Xodim(Ismi=Ismi,manzili=manzili,maoshi=maoshi))

for xodim in xodimlar:
    xodim.maosh()