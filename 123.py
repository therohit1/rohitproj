'''userword=input("Enter your name : ")
userword=userword.upper()
for r in userword:
    if r=='A' or r=='E' or r=='I' or r=='O' or r=='U': 
        continue
    print("Remaining letters:",r)'''
'''
name=input("Enter your name :")
name=name.upper()
new=name
vovels=('A','E','I','O','U')
for r in name:
    for r in vovels:
        new=new.replace(r,"")
print(new)'''
