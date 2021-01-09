# program to print the odd nos.
#i=1
#n=int(input("Enter your no.:"))
#while i<n:
    #print(i*i)
    #i+=2

#program to print even nos.
#i=2
#while i<10:
    #print(i*i)
    #i+=2

#program to print prime or not
#i=2
#n=int(input("Enter your no:"))
#while i<n:
    #if n%2==0:
        #print("Not a prime no.")
        #exit(0)
    #i+=1
#print("Prime No.")

#program to print factorial no
#n=int(input("Enter your no:"))
#i=1
#fact=1
#while i<=n:
    #fact=fact*i
    #i+=1
#print(fact)

#program to print fibonacci series
#n=int(input("Enter your no:"))
#n1=1
#print(n1)
#n2=1
#print(n2)
#n3=0
#i=1
#while i<=n:
    #n3=n1+n2
    #print(n3)
    #n1=n2
    #n2=n3
    #i+=1

#print table of given no.
'''
i=1
n=int(input("your no :"))
while i<11:
    print(f'{n} x {i} = {n*i}')
    i+=1
'''
#program to get sum of digits eg 123=6
'''
n=int(input("Enter digits:"))
sum=0
rem=0
while n>0:
   rem=n%10
   n=n/10
   sum=sum+rem
print(int(sum))
'''
#program to find sum of odd nos between 20 to 50
'''
i=2
while 20<50:
    if i%2==1:
        print(i,"+",i,"=",i+i)
    i+=2
'''
#program to find sum of even nos between 20 to 50
'''
i=2
while i<50:
    if i%2==0:
        print(i+i)
    i+=2
'''