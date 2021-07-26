EnUz = {
  "i": "men",
  "you": ["sen", "siz"],
  "he": "u",
  "she": "u",
  "it": "u",
  "we": "biz",
  "they": "ular",
  "teacher": "o'qituvchi",
  "pupil": "o'quvchi",
  "hello": "salom",
  "bye": "xayir",
  "world": "dunyo",
  "uzbekistan": "O'zbekiston"
}
txt=input("Inglizcha zo'z kiriting:")
if txt in EnUz.keys():
  print(EnUz[txt])
else:
  print("Bunday so'z lug'atda yo'q")

