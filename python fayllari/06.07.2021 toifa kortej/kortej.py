"""kortejlar (tuple)"""
numbers = (1, 2, 3, 4)
numbers1 = [1, 2, 3, 4]
print(type(numbers))
print(type(numbers1))
print("------------------------------->")
""" konstruktor """
a = tuple([1, 2, 3, 4])
print(type(a))
print("------------------------------->")
""" kortej elementlariga murojaat """
numbers = (1, 2, 3, 4)
print(numbers[2])
print("------------------------------->")
# bu amallar indexlar orqali amalga oshiriladi
""" kortejda yangilashni faqat ro'yxatga o'tkazib, keyin bajarsa bo'ladi """
numbers = (1, 2, 3, 4)
numbers = list(numbers)
numbers[1] = 9
numbers = tuple(numbers)
print(numbers)
print("------------------------------->")
""" kortej elementlarini looplar (for, while) yordamida alohida qilib chiqarish """
numbers = (1, 2, 3, 4)
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
for i in numbers:
    print(i)
print("------------------------------->")
# fordan indeks bo'yicha foydalanish
for i in range(len(numbers)):
    print(numbers[i])
print("------------------------------->")
""" kortejlarni qo'shish """
numbers1 = (1, 2, 3, 4)
numbers2 = (5, 6, 7, 8)
numbersAll = numbers1 + numbers2
print(numbersAll)
print("------------------------------->")
""" kortejlarni songa ko'paytirish """
numbers = (1, 2, 3, 4)
myNumbers = numbers * 2
print(myNumbers)
print("------------------------------->")
""" kortej metodlari """
# count()
numbers = (1, 2, 3, 4, 4, 3, 2, 2)
print(numbers.count(2))
print("------------------------------->")
# index
print(numbers.index(2))
print("------------------------------->")
# masala
x = (1)
y = (1, )
print(type(x))
print(type(y))
print("------------------------------->")
# Yo'qlik qiymatlar
a = None
b = ''
c = []
d = ()
e = 0
h = False
print(f"{bool(a)} {bool(b)} {bool(c)} {bool(d)} {bool(e)} {bool(h)}")
print("------------------------------->")