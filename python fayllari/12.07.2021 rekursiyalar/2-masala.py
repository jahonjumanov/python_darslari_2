n=input("n=")
def daraja(n):
    qiymat=[]
    for i in range(1,n):
        if i**2<n:
            qiymat.append(i)
    return qiymat
print(daraja(n))