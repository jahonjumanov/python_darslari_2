"""# 1 - masala.
# 1. o'quvchilar ro'yhatini e'lon qiling unga oxiriga yangi o'quvchi qo'shing (print qiling) append
# 2. keyin o'rtasiga yangi o'quvchi qo'shing (print qiling) insert
# 3. o'quvchilar sonini toping (print qiling) len
# 4. o'quvchilar ro'yhatiga yana bor ismlardan birini kiriting
#    va shu ismli o'quvchi nechtaligini toping (print qiling) append yoki insert , count
# 5. yangi o'quvchilar ro'yhatini e'lon qilib eski ro'yhatga ulang
#    va eski ro'yhatni (print qiling) extend
# 6. ixtiyoriy o'quvchini indeksini topib bering (print qiling) index
# 7. ro'yhatni tozalang (print qiling) clear"""
uquvchi=["Ilxom","Jasur","Ilxom"]
uquvchi.append("Sobir")
print(uquvchi)
uquvchi.insert(1,"Sanjar")
print(uquvchi)
print(len(uquvchi))
print(uquvchi.count("Ilxom"))
uquvchi2=["Xosilbek","Kamol","Nosir"]
uquvchi.extend(uquvchi2)
print(uquvchi)
print(uquvchi.index("Jasur"))
uquvchi.clear()
print(uquvchi)
