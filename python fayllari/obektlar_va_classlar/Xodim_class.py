class Xodim:
    def __init__(self, Ismi,Familiyasi,tugulgan_yili,ish_joyi,manzili,maoshi):
        self.Ismi=Ismi
        self.Familiyasi=Familiyasi
        self.tugulgan_yili=tugulgan_yili
        self.ish_joyi=ish_joyi
        self.manzili=manzili
        self.maoshi=maoshi
Uqituvchi=Xodim("Jahongir","Jumanov",1994,"45-maktab","Baxmal tumani",2500000)
Quruvchi=Xodim("Jasurbek","Alishev",1990,"MCHJ","Gallarol tumani",1500000)
print(Uqituvchi.Ismi)
print(Uqituvchi.__dict__)
print(Quruvchi.Familiyasi)
print(Quruvchi.__dict__)