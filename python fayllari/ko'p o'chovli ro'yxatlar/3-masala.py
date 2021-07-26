# 3*3 matrisa qo'shish
matrix=[[1,2,4],[3,4,6],[4,7,9]]
matrix1=[[2,4,9],[5,7,8],[7,8,12]]
matrix2=[[3,7,9],[5,9,8],[12,8,8]]
b=[[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(3):
    for j in range(3):
        b[i][j]=matrix[i][j]+matrix1[i][j]+matrix2[i][j]
for son in b:
    print(son)