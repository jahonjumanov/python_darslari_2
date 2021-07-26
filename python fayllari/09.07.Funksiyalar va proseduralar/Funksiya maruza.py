
"""def Salom():
    print("Mening ismim Jahongir")
# funksiani chaqirish
Salom()"""
# argument va parametr
# 1.funksiyani e'lon qilish
"""def Salom(men): # bu yerda parametr
    print(f"Mening ismim {men}")"""
# 2.Funksiani chaqirish
"""Ism=input("Ism kiriting")
Salom(Ism)"""
# Ko'p o'zgaruvchili parametrlar
"""def toliq_ism(Ism,Familiya):
    toliq=Ism + " " +Familiya
    print(toliq)
toliq_ism("Jahongir","Jumanov")
toliq_ism("Ilhom","Jumashev")
"""
"""*:args -> bu parametrlar toplami"""
"""def ismlar_ruyxat(*ism):
    print(ism)
ismlar_ruyxat("Jasur", "Sanjar","Ilhom","Nosir")"""

"""def fanlar_ruyxat(*fan):
    print(fan)
fanlar_ruyxat("Matematika","Fizika","Informatika")"""
