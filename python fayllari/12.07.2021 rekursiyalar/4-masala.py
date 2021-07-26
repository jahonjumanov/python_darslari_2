n=int(input("n="))
#1-usul
def nyulduz(b):
    for i in range(b):
        print("*"*b)
nyulduz(n)
print("--------------------------------------->")
#2-usul
def nyulduz(n):
    print(("*"*n+'\n')*n)
nyulduz(n)