try:
    n=int(input("Son kiriting:"))
    if n%2==0:
        raise Exception()
except:
    print("xato chunki jaft son")
else:
    print("yaxshi siz toq son kiritingiz")
finally:
    print("dastur yakunlandi")