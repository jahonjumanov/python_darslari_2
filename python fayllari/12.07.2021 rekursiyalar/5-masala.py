n=int(input("n="))
def nboluvchi(n):
    txt=''
    for i in range(1, n + 1):
        if n % i== 0:
            txt+=str(i)+' '
    print(txt)
nboluvchi(n)
