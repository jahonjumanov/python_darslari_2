# ikkita sonni kattasini topuvchi funksiya
a=int(input("1-son="))
b=int(input("2-son="))
def katta(a,b):
    if a>b:
        return a
    else:
        return b
print(katta(a,b))