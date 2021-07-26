n = int(input("n = "))
def raqam_yigindi(a):
    yuz=n//100
    un=n%100//10
    bir=n%10%10
    print(yuz+un+bir)
raqam_yigindi(n)