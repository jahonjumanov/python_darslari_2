b=[[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(3):
    for j in range(3):
        b[i][j]=int(input(f"B[{i}][{j}]="))
print(b)
for i in b:
    print(i)
for i in b:
    for j in i:
        print(j)