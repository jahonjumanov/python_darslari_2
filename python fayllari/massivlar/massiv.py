# bugungi mavzu massivlar->Array
#python aynan massiv tushuncha yo'q
'''a="12345678"
b=12345
sonlar=[1,2,3,4,'salom',True,[5,6,7],2.6]
print(type(sonlar))'''
'''#pythonda massiv o'rniga ro'yxatdan foydalaniladi
#Ro'yxatning massivdan asosiy farqi bu turli xil toifali elementlariga ega bo'lishi mumkin
#list->ro'yxat
#ro'yxat elementiga murojat
ruyxat_elementlari=sonlar[4]
print(ruyxat_elementlari)'''
'''"ruyxat elementini yangilash"
mashinalar=["malibu","laceti","nexia"]
#yangilash
mashinalar[0]="damas"
print(mashinalar)'''
"""mevalar=["olma","olcha"] #mevalar =['olma', 'olcha', 12]
mevalar.append(12)
print(mevalar)
# xulosa-> append massivning oxirgi elementini qo'shadi"""
'''#Ruyxatni tozalash
son=[2,3,5,7]
son.clear()
print(son)'''
'''# ro'yxat elementlarin boshqa royxatga copiya qilish
son=[2,3,5,7]
sonlar=son.copy()
print(sonlar)'''
'''#Ruyxatda bir xil elementlarni sanash->count() methodi
son=[2,2,2,3,4,5,6,3,5,7]
print(son.count(2))'''
'''# extend() bu ruyxatda boshqa ruyxatni ulash
son=[2,3,5,7]
son1=[9,12,5,7]
son.extend(son1)
print(son)'''
'''# index()-> bu elementni indexs o'rnini aniqlaydi
sonlar=[1,2,3,4,'salom',True,[5,6,7],2.6]
print(sonlar.index(2.6))'''
'''#insert()methodi -> bu element o'zingiz xoxlagan index elementini qo'shish
son=[5,6,3,9]
son.insert(4,2)
print(son)'''
'''#pop-> berilgan indexsini elementini o'chirish
son=[5,6,3,9]
son.pop(2)
print(son)'''
# remove -> beilgan elementni nomi bo'yicha o'chirish
mashina=["BMW", "Arlando","Xunday","Mers"]
mashina.remove("BMW")
print(mashina)

print(mashina)

