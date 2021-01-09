#Python Shortcut
n=int(input('Enter a number: '))
r=int(str(n)[::-1])
print(r)

#Traditional method
n=int(input('Enter your number: '))
rev=0
rem=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
