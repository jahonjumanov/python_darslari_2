a = (1, 2, 3, 4, 5, 6, 7, 8,23,3,3,33,12,23)
b = list(a)
c = []
for i in range(len(b)):
    c.append(b[0])
    if b[0] == b[-1]:
        break
    c.append(b[-1])
    b.pop(0)
    b.pop(-1)
    if not b:
        break
a = tuple(c)
print(a)