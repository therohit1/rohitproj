#program to print odd nos.
#n=int(input("Enter your no:"))
#for i in range(1,n+1,2):
#    print(i)

#program to print even nos
#for i in range(2,51,2):
 #  print(i)

#print Table of a given no.
#n=int(input("Enter your no:"))
#for i in range(1,11):
    #print(n,"x",i,"=",i*n)

#Use of Pass,Break,Continue
#for i in range(1,10,2):
    #pass
'''
for letter in "mrwaghmarerohit":
   if letter=="e":
        break
   print(letter)
'''
'''
for i in range(1,10,2):
    if i%3==0:
        continue
    print(i*i)
'''
#calculating factorial
'''
n=int(input("Enter your no:"))
fact=1
for i in range(1,n+1):
   fact=fact*i
print(fact)
'''
#programm to find prime or not
#n=int(input("Enter your no : "))
#for i in range(1,n):
   # if n%2==0:
   #     print("Not a prime no")
    #    exit(0)
#print("Prime no")
#

#program to get fibonacci series
'''
n=int(input("Enter your no."))
n1=1
n2=1
print(n1," ",n2,end="\t")
n3=0
for i in range(1,n+1):  
    n3=n1+n2
    print(n3,end="\t")
    n1=n2
    n2=n3
'''
#program to create table of given no.
#n=int(input("Your No :"))
#for i in range(1,11):
    #print(n,"x",i,"=",n*i)

#Finding sqrt of given nos from list
#numbers=[4,9,16,25,36]
#for n in numbers:
 #   print("Sqrt of",n,"is",round(n**0.5))

#finding cube of all nos
#for i in range (1,10+1,1):
#   print(i,"x",i,"x",i,"=",i*i*i)

#wap to print 15 19 23 27 31
'''a=15
for i in range(1,6):
    print(a,end=" ")
    a+=4'''
#wap to print 33 39 45 51 57
'''
a=33
for i in range(1,6):
    print(a)
    a+=6
'''

#wap to print 5 15 10 10 15 5
'''
a=5
b=15
for i in range (1,7):
    if i%2==0:
        print(b,end=" ")
        b-=5
    else:
        print(a,end=" ")
        a+=5
'''

#Printing Co-ordinates
'''(x,y)
   (0,0)
   (0,1)
   (0,2)
   (1,0)
   (1,1)
   (1,2)'''
'''for x in range(4):
    for y in range(3):
        print(f'({x},{y})')'''


for letter in "mrwaghmarerohit":
   if letter=="e":
        break
   print(letter,end=' ')


for i in range(1,10,2):
    if i%3==0:
        continue
    print(i*i)