#28/03/2020
#Yogesh
'''
n=int(input("Enter your no :"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
'''
'''
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#Yogesh
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
#Shivkumar
number=[1,2,4,4,1,4,2,6,2,9]
unique=[]
for num in number:
    if num not in unique:
        unique.append(num)
print(unique)
'''
#30/03/2020
#Yogesh 
'''

'''
#Sum series:

def sum(n):
    for i in range(1,n+1):
        if n<=1:
            return n
        else:
            return n+sum(n-i)

n=int(input("Enter your number :"))
print(sum(n))