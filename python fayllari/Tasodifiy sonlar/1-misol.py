import random
'''for i in range(10):
    print(round(random.random()))'''
# 1-masala  1 da 10 gacha bo'lgan butun son kiriting
#va randint bilan genaratsiya qilingan son bilan solishtiring
kiritilgan_son=int(input("son->"))
tasodifiySon=random.randint(1,10)
if kiritilgan_son==tasodifiySon:
    print(tasodifiySon)
    print("yuttingiz")
else:
    print(tasodifiySon)
    print("qaytaurinib ko'ring")