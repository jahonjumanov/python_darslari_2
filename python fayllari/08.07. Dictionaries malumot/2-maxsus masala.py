shaxs=[
    {
        "Ismi":"Alisher",
        "Yosh":27
    },
    {
        "Ismi":"Aziza",
        "Yosh":24
    },
    {
        "Ismi":"Xusan",
        "Yosh":12
    }
]
v=[]
for i in shaxs:
    v.append(i["Ismi"])
for i in v:
    if i[0]=="A":
        print(i)


