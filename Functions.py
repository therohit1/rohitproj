#FUNCTIONS 
'''def p():
    return("Hello rohit")
print(p())'''
'''
def add():
    a=5
    b=6
    return(a+b)
print(add())'''
'''
def even_or_odd():
    if a%2==0:
        return("Even")
    else:
        return("Odd")
a=int(input("Enter a value:"))
print(even_or_odd())        '''
#-----------------------------------------------------------------------------------------
#Factorial
'''def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return(fact)
a=int(input("Enter your no:"))
print(factorial(a))'''
#--------------------------------------------------------------------------------------------------
#Prime or not
'''def prime_or_not(n):
    j=2
    while j<=n:
        if n%2==0:
            return("Not a prime")
            exit(0)
        j+=1
    return("Prime")
n=int(input("Enter a no:"))
print(prime_or_not(n))'''
#or#
'''def prime_or_not(n):
    for i in range(2,n):
        if n%i==0:
            return("Not prime")
            exit(0)
    return("prime")
n=int(input("Enter a no:"))
print(prime_or_not(n))'''

#or Using flag#
'''def prime_or_not(n):
    flag=0
    for i in range(1,n+1):
        if n%i==0:
            flag+=1
    if flag==2:
        return("Prime")
    else:
        return("Not a Prime")

n=int(input("Enter your no:"))
print(prime_or_not(n))'''

#Calculating all of prime nos
'''def primes(n):
    for i in range(1,n+1):
        flag=0
        for j in range(1,i+1):
            if i%j==0:
                flag+=1
        if flag==2:
            return(n)
    print("\n")
n=int(input("Enter your no:"))
print(primes(n))'''
#----------------------------------------------------------------------
#Fibonacci Series
'''def Fibonacci(n):
    n1=1
    n2=1
    print(n1,n2)
    for i in range(1,n+1):
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
n=int(input("Enter your no:"))
print(Fibonacci(n))'''
#----------------------------------------------------------------------
#Armstrong 
'''def armstrong_or_not(n):
    c=0
    a=n
    while n>0:
        rem=n%10
        c=c+pow(rem,3)
        n=n//10
    if a==c:
        return("armstrong")
    else:
        return("Not")
n=int(input("Enter a no:"))
print(armstrong_or_not(n))'''

#Calculating armstrong nos from given range
'''def armstrong_nos():
    for n in range(1,1001):
        c=0
        a=n
        while n>0:
            rem=n%10
            c=c+pow(rem,3)
            n=n//10
        if a==c:
            print(a)
#n=int(input("Enter your no:"))
print(armstrong_nos())'''
#---------------------------------------------------------------------
#Using Recursive function
'''
def pallindrome(a):
    #a=int(input("Enter your number :"))
    b=a[::-1]
    if a==b:
        print("Pallimdrome")
    else:
        print("Not pallindrome")

a=input("Enter a number:")
pallindrome(a)
'''
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
#---------------------------------------------------------------------------------
#Sum series:
'''
def sum(n):
    for i in range(1,n+1):
        if n<=1:
            return n
        else:
            return n+sum(n-i)

n=int(input("Enter your number :"))
print(sum(n))
'''
#-------------------------------------------------------------------------------
#Area of triangle
'''
def aot(a,b):
    c=(1/2)*a*b
    print("AOT :",c)
b=int(input("Enter base :"))
h=int(input("Enter height :"))
aot(b,h)
'''
#-------------------------------------------------------------------
#Calculate square and cube
'''
def square(a):
    s=a*a
    return s
def cube(a):
    #c=a**3
    c=pow(a,3)
    return c
a=int(input("Enter your value :"))
sq=square(a)
cub=cube(a)
print(sq," ",cub)
'''
#------------------------------------------------------------------
#Function using Positional and Default Argument
#Positional
'''
def person(name,age):
    print(name)
    print(age)
person(age=22,name='rohit')

#Default
def person(name,age=22):
    print(name)
    print(age)
person("Rohit")
'''
#---------------------------------------------------------------------
#Scope of variable inside a function
'''
a=10
def p():
    a=15
    print(a)
p()
print(a)
'''
#---------------------------------------------------------------------
#WAP using method to check prime or not using class
'''
class one:
    def prime(self):
        c=0
        n=int(input("Enter a number :"))
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        if c==2:
            print("Prime ")
            
        else:
            print("Not Prime")
x=one()
x.prime()
'''
#WAP method to add and multiply a number using class
'''
class one:
    def add(self,x,y,z):
        print(x+y+z)
    def cube(self,p):
        print(p**3)
    def multiply(self,x,y,z):
        print(x*y*z)
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
x=one()
x.add(a,b,c)
x.cube(c)
x.multiply(a,b,c)
'''

def add(x,y):
    c=x+y
    print(c)

add(3,4)