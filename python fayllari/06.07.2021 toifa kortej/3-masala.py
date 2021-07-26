"""kortej berilgan ularning o'rta arifmetigini  topish"""
numbers=(1,2,3,4,5,6,9,8,7,4,6,5)
#print(round(sum(number)/len(number)))
i=0
S=0
for number in numbers:
    i+=1
    S+=number
print(S/i)