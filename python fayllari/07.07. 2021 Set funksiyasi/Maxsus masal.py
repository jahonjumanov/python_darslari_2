import random as rd

A = []
B = []
C = []
# A va b to'plamlarni birlashmasini olib C to'plam bilan kesishmasini olasiz

for i in range(10):
    k = rd.randint(1, 10)
    A.append(k)

for i in range(10):
    k = rd.randint(1, 10)
    B.append(k)

for i in range(10):
    k = rd.randint(1, 10)
    C.append(k)

print(A)
print(B)
AUB = set(A + B)
print(AUB)

AUB = list(AUB)
C = set(C)
print(C)

D = []

for i in C:
    if i in AUB:
        D.append(i)

D = set(D)