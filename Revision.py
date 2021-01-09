#Addition,Subtraction,Multiplication,Division
'''
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
n=int(input("Enter your choice :"))
if n==1:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    print("Adition is :",num1+num2)
#------------------------------------------------
elif n==2:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    print("Subtraction is :",num1-num2)
#------------------------------------------------    
elif n==3:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    print("Multiplication is :",num1*num2)
#------------------------------------------------
elif n==4:
    num1=int(input("Enter your 1st number:"))
    num2=int(input("Enter your 2nd number:"))
    print("Division is :",num1/num2)
#if n!=1 or n!=2 or n!=3 or n!=4:
else:
    print("Invalid choice")
'''
#---------------------------------------------------------------------------------------------------
'''
print("1.Factorial")
print("2.Prime or not ")
print("3.Prime or not using flag")
print("4.Pallindrome")
print("5.Armstrong or not")
print("6.Even or odd")
print("7.Fibonacci series")

n=int(input("Enter your choice :"))

if n==1:#Factorial
    num=int(input("Enter your number :"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial is :",fact)
#------------------------------------------------
elif n==2:#Prime or not using while loop
    num=int(input("Enter your no :"))
    i=2
    while i<=n:
        if num%2==0:
            print("It's composite number")
            exit(0)
    print("Prime number")
#------------------------------------------------
elif n==3:#Prime or not using For loop
    num=int(input("Enter your number :"))
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        print("Prime number")
    else:
        print("It's a composite number")
#-----------------------------------------------
elif n==4:#Pallindrome
    num=int(input("Enter your number :"))
    a=num
    rem=0
    rev=0
    while num>0:
        rem=num%10
        num//=10
        rev=rev*10+rem
    if a==rev:
        print("It's a pallindrome number")
    else:
        print("It's not a pallindrome number")
#----------------------------------------------
elif n==5:#Armstrong
    num=int(input("Enter your number :"))
    a=num
    rem=0
    c=0
    while num>0:
        rem=num%10
        c=c+pow(rem,3)
        num//=10
    if a==c:
        print("It's an Armstrong number")
    else:
        print("It's not an Armstrong number")
#----------------------------------------------
elif n==6:#Even or odd
    num=int(input("Enter your number"))
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")
#----------------------------------------------
elif n==7:#Fibonacci series
    num=int(input("Enter your number :"))
    n1=1
    n2=1
    n3=0
    print(n1,n2,end=" ")
    i=1
    while i<=num:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        i+=1
else:
    print("Invalid choice")
'''
#-------------------------------------------------------------------------------------------
'''
print("1.Prime nos between given range")
print("2.Armstrong nos between given range")
n=int(input("Enter your choice :"))
if n==1:#
    num=int(input("Enter your range :"))
    for i in range(1,num+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            print(i)
    print("\n")
elif n==2:#Armstrong nos from 1 to 1000 -->,1,153,370,371,407
    for num in range(1,1001):
        a=num
        c=0
        while num>0:
            rem=num%10
            c=c+pow(rem,3)
            num//=10
        if a==c:
            print(a)
'''
#----------------------------------------------------------------------------------------------
#All patterns
#n=int(input("Your number :"))
'''for i in range(1,n+1):#right angle tri
    print(i*"*")'''
#--------------------------------------
'''for i in range(n,0,-1):
    print("*"*i)'''
#--------------------------------------
'''for i in range(1,n+1):
    print((n-i)*" "+"*"*i)'''
#--------------------------------------
'''for i in range(n,0,-1):
    print((n-i)*" "+"*"*i)'''
#--------------------------------------
'''for i in range(1,n+1):
    print("*"*i)
for j in range(n-1,0,-1):
    print("*"*j)'''
#--------------------------------------
'''for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for j in range(n-1,0,-1):
    print(" "*(n-j)+"*"*j)'''
#-------------------------------------
'''for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))'''
#-------------------------------------
'''for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)'''


t= [[3-i for i in range(3)] for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
print(s)