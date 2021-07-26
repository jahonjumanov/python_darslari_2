import random
 #1-masala  1 da 10 gacha bo'lgan butun son kiriting
#va randint bilan genaratsiya qilingan son bilan solishtiring
imkoniyat=1
while imkoniyat<=5:
    tasodifiySon = random.randint(1, 10)
    kiritilgan_son = int(input("son->"))
    for i in range(1, 5):
    if kiritilgan_son==tasodifiySon:
        print("yuttingiz")
        break
    imkoniyat+=1
    else:
        print("qaytaurinib ko'ring")