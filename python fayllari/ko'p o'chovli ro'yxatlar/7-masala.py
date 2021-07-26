# 1-usul matrisa elementlarini bir satrga joylashtirish
b=[[12,5],[3,2]]
print(b[0]+b[1])
# 2-usul
b=[[12,5],[3,2]]
c=[]
for i in b:
    for j in i:
        c.append(j)
print(c)
