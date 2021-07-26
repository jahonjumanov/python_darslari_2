shaxslar = [
    {
        "otasi_ismi":"Xasan",
        "ism": "Shoxzod",
        "yoshi": 20,
        "jinsi": "erkak"
    },
    {
        "otasi_ismi":"Juman",
        "ism": "Jahongir",
        "yoshi": 22,
        "jinsi": "erkak"
    },
    {
        "otasi_ismi":"Mansur",
        "ism": "Zamira",
        "yoshi": 22,
        "jinsi": "ayol"
    },
    {
        "otasi_ismi":"Jasur",
        "ism": "Madinabonu",
        "yoshi": 13,
        "jinsi": "ayol"
    }
]
for i in shaxslar:
    if i["jinsi"]=="erkak":
        i["familiyasi"]=i["otasi_ismi"]+"ov"
    else:
        i["familiyasi"] = i["otasi_ismi"] + "ova"
    print(i)