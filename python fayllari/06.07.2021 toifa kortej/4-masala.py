"""kortej berilgan ularning toq o'rindagi elementlari """
d=(1,2,3,4,5,6)
juft=[]
for i in range(1,len(d),2):
    juft.append(d[i]**2)
print(tuple(juft))


