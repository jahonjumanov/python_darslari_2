# """ xatolar bilan ishlash yoki istisnolar """
#
# # SyntaxError
# print("hello",,
#
# # IdentationError:
# for i in range(5):
# print(i)
# # NameError
# try:
#     ism = "Oybek"
#     print(ims)
# except:
#     print("xato -> NameError")
# # valueError
# try:
#     x = "1.2"
#     int(x)
# except:
#     print("ValueError")

# try -> urunib ko'rmoq
# except -> istisno qilish

# """ bir necha istisnolar """
# try:
#     # nameError
#     ism = "Oybek"
#     print(ism)
#     # valueError
#     i = '1.02'
#     int(i)
# except NameError:
#     print("ism o'zgaruvsini nomida xato")
# except ValueError:
#     print("qiymatda xatolik")

# """ else -> kodingiz to'g'ri ishlaganda chiqadigan natija"""
"""#
# try:
#     print("inson holati: ", end=" ")
#     print(x)
# except:
#     print("inson kasal")
# else:
#     print("soppa - sog'")"""

#""" finally -> try except jarayoni tagagundan so'ng ishlatiladi"""
"""y = 0
try:
    y = 0

    print("salom")
except:
    y += 1
    print("try dagi nimadur xato")
finally:
    if y == 0:
        print("dasturda xato yo'q")
    else:
        print("dasturda xato bor")"""
