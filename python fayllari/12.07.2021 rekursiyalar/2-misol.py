#fibonachi sonlarini n - chi xadini topshish:
# 1, 1, 2, 3, 5, 8 ...
a = []
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def fib_hadlari(n):
    for i in range(1, n + 1):
        print(fib(i), end=" ")


fib_hadlari(9)