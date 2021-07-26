class Xodim:
    def init(self, ism, manzili, maoshi):
        self.ism = ism
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(self):
        print(f"Mening ismim {xodim.ism} maoshim {xodim.maoshi}")
        if self.maoshi < 1000000:
            print("Mening oyligim kam!!!")


xodimlar = []

n = int(input("Xodimlar soni: "))
for i in range(n):
    print(f"{i + 1} - xodim")
    ism = input("Ism kiriting: ")
    manzili = input("Manzil kiriting")
    maoshi = int(input("Maoshini kiriting"))
    xodimlar.append(Xodim(ism=ism, manzili=manzili, maoshi=maoshi))



for xodim in xodimlar:
    xodim.gap()