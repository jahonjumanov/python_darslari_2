"""Class yaratish"""
# class son():
#     x=1
#     y=2
# son1=son()   # son1-> bu obeklar, son()->klass
# print(son1.x)
# print(son1.y)
# son2=son()
# print(son2.x)
# Xulosa. Bitta klasdan hohlagancha obekt olish mumkin

"""def __init__(self) funksiyasi:"""
class son():
    def __init__(self,x,y):
        self.x=x
        self.y=y
son3=son(4,5)
print(son3.x, son3.y)
son4=son(7,8)
print(son4.x,son4.y)

 """obekni birnechta elementini o'chirish"""
# del son3.x
# print(son3.__dict__)
# obekni o'zini o'chirish
# del son3
# print(son3.__dict__)


""" classda metodlar """


class Avtomobil:
    def __init__(self, rusumi):
        self.rusumi = rusumi

    def signal(self):
        print("Biiib!!!!")


malibu = Avtomobil("Malibu")
malibu.signal()


class Shaxs:
    def __init__(self, ism, fam):
        self.ism = ism
        self.fam = fam

    def tuliq_ism(self):
        return self.ism + ' ' + self.fam


sh1 = Shaxs("Oybek", "Narzullaev")
print(sh1.tuliq_ism())