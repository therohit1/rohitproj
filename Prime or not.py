# using while loop
'''
n=int(input("Enter your no. :"))
i=2
while i<n:
    if n%i==0:
        print("Not a prime")
        exit(0)
    i+=1
print("Prime")
'''
# using for loop
'''
n=int(input("Enter your no:"))  
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("Not prime")
'''
# or
#using for else
'''
n=int(input("no:"))
for i in range(2,n):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("Prime")
'''
