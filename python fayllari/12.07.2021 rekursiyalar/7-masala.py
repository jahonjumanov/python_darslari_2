import math
x1=int(input("x1="))
x2=int(input("x2="))
x3=int(input("x3="))
x4=int(input("x4="))
x5=int(input("x5="))
def sport(x1,x2,x3,x4,x5):
  eng_katta=max(x1,x2,x3,x4,x5)
  eng_kichik=min(x1,x2,x3,x4,x5)
  urtacha_arifmetik=(x1+x2+x3+x4+x5-eng_kichik-eng_katta)/3
  print(f"eng_katta={eng_katta},eng_kichik={eng_kichik},O'rtacha arifmetik={urtacha_arifmetik}")
sport(x1,x2,x3,x4,x5)