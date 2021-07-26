def fun(x):
    if x==0:
        return 0
    elif x%2==0:
        return 1
    elif x%2==1:
        return -1
x=int(input("x son="))
x=fun(x)
print(x)