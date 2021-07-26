fam=input('Familiya kiriting=')
if fam[-2]=='o' or fam[-3]=='p':
    fam = fam.replace(fam[-1]," ")
    fam = fam.replace(fam[-2]," ")
    fam = fam.replase(fam[-3]," ")
print(fam)