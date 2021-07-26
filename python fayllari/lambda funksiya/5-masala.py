# kiritilgan ismni n marta takrorlash
#1-usul
a=input("Ism kiriting:")
ism=lambda a:(a+' ')*2
print(ism(a))
#2-usul
#
def ism(a):
    return lambda n:(a+' ')*n
n=ism(a)
print(n(5))