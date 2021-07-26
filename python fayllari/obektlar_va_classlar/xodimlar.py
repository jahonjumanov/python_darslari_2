# class Xodim:
#     def __init__(self, Ismi,manzili,maoshi):
#         self.Ismi = Ismi
#         self.manzili = manzili
#         self.maoshi = maoshi
# x1 = Xodim("Jahongir", "Baxmal tumani", 2500000)
# x2 = Xodim("Jasur", "G'allarol tumani", 1500000)
# x3 = Xodim("Nodir", "Zaribdor tumani", 2300000)
# x4 = Xodim("Ilhom", "Zomin tumani", 1800000)
# x5 = Xodim("Jamshid", "Baxmal tumani", 2200000)
# xodimlar=[]
# print(x1.Ismi,x1.manzili,x1.maoshi)
# xodimlar.append(x1)
# print(x2.Ismi,x2.manzili,x2.maoshi)
# xodimlar.append(x2)
# print(x3.Ismi,x3.manzili,x3.maoshi)
# xodimlar.append(x3)
# print(x4.Ismi,x4.manzili,x5.maoshi)
# xodimlar.append(x4)
# print(x5.Ismi,x5.manzili,x5.maoshi)
# xodimlar.append(x5)
# for xodim in xodimlar:
#     if xodim.maoshi>2000000:
#         print(xodim.)

 # 2-usul
class Xodim:
    def __init__(self, Ismi,manzili,maoshi):
        self.Ismi = Ismi
        self.manzili = manzili
        self.maoshi = maoshi
    def maosh(self):
        print(f"Mening ismim {self.Ismi}, Maoshim {self.maoshi}")
xodimlar=[]
x1 = Xodim("Jahongir", "Baxmal tumani", 2500000)
xodimlar.append(x1)
x2 = Xodim("Jasur", "G'allarol tumani", 1500000)
xodimlar.append(x2)
x3 = Xodim("Nodir", "Zaribdor tumani", 2300000)
xodimlar.append(x3)
x4 = Xodim("Ilhom", "Zomin tumani", 1800000)
xodimlar.append(x4)
x5 = Xodim("Jamshid", "Baxmal tumani", 2200000)
xodimlar.append(x5)
for xodim in xodimlar:
    xodim.maosh()

