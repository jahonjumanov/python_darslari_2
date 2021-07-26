x=int(input("x nuqtani kiriting="))
y=int(input("y nuqtani kiriting="))
if x<4 and x>0 and y<4 and y>0:
    print("birinchi chorak ichida")
elif x>4 and y>4 or x>0 and y>0:
    print("birinchi chorak tashqarisida")
elif x<0 and x>-4 and y<4 and y>0:
    print("ikkinchi chorak ichida")
elif x>-4 and y>4 or x<0 and y>0:
    print("ikkichi chorak tashqarisida")
elif x<0 and x>-4 and y>-4 and y<0:
    print("uchinchi chorak ichida")
elif x<-4 and y<-4 or x<0 and y<0 :
    print("uchinchi chorak tashqarisida")
elif x<0 and x<4 and y<0 and y<-4:
    print("tortinchi chorak ichida")
elif x==0 and y==0:
    print("kordinata boshida")
elif x==0 and y>0:
    print
else:
    print("to'rtinchi chorakdan tashqarisida")