#Pallindrome
''' 
n=int(input("Enter your no:"))
rem=0
rev=0
a=n
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
#print(rev)
if a==rev:
    print("Pallindrome")
else:
    print("Not pallindrome")
'''
#Reversal of digits
'''
n=int(input("Enter a num:"))
rem=0
rev=0
while n>0:
    rem=n%10
    print(rem,end="")
    n=n//10
'''
#or
'''
def pallindrome(a):
    b=a[::-1]
    if a==b:
        print("Pallindrome")
    else:
        print("Not pallindrome")

a=input("Enter a number:")
pallindrome(a)
'''
#or
'''
def palindrome(s):
    if len(s) < 1: 
        return True
    else:
        if s[0] == s[-1]: 
            return palindrome(s[1:-1]) 
        else: 
            return False
a=str(input("Enter string :"))

if(palindrome(a)==True): 
    print("Palindrome !")
else:
    print("Isn't a palindrome !")
'''

# or
'''
rev=0
def pallindrome(n):
    global rev
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
n=int(input("Enter your no:"))
rev=pallindrome(n)
if n==rev:
    print("Pallindrome")
else:
    print("Not a pallindrome")
'''
