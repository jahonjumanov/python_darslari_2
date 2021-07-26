""" ro'yhat argument sifatida """


def uquvchilar(x):
    for i in x:
        print(i)


uquvchi = []
k = int(input("o'quvchilar sonini kiriting: "))

for i in range(k):
    ism = input(f"{i + 1} - o'quvchi ismi: ")
    uquvchi.append(ism)

uquvchilar(uquvchi)