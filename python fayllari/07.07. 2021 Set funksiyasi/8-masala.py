# olimpidaga qatnashgan o'quvchilarni ruyxatini topish
matematika=["Jahongir","Jasurbek","Ilhom"]
fizika=["Ali", "Jahongir","Begzod","Jasurbek"]
Informatika=["Ilhom","Begzod","Zafar"]
fanlar=matematika+fizika+Informatika
fanlar=set(fanlar)
print(fanlar)
print(len(matematika))
print(len(fizika))
print(len(Informatika))
print(len(set(matematika+fizika)))
print(len(set(fizika+Informatika)))
print(len(set(matematika+Informatika)))
print(len(fanlar))
