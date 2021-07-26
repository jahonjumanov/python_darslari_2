import datetime as dt
# print(dir(datetime))
# print(datetime.date.today())
# print(datetime.datetime.now())
# print(dt.datetime.now().year)
# vaqt=dt.datetime.now()
# print(vaqt.year)
# print(vaqt.month)
# print(vaqt.day)
# print(vaqt.weekday())
# print(vaqt.hour)
# print(vaqt.minute)
# print(vaqt.second)
# print(vaqt.microsecond)


# def soat(vaqt):
#     print(f"soat: {vaqt.hour}:{vaqt.minute}:{vaqt.second} bo'ldi")
# soat(vaqt)

x=dt.datetime.now().second
while True:
    if x+5==dt.datetime.now().second:
        print("Salom")
        x=dt.datetime.now().second
        break