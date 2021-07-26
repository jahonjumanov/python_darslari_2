#
x=input("Ism kiriting")
if x[-1]=='a' or x[-1]=='e' or x[-1]=='i' or x[-1]=='o' or x[-1]=='u':
  print(x + "yev")
else x[-1]=='f':
 print(x[-1].replace('f','p')+'ov')