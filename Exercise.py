'''n=int(input("Enter your no:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print( )'''

#Alternate way
'''n=5
j=1
while j<=n:
    for i in range(1,j+1):
        print(j,end=" ")
    print()
    j+=1'''

#Using 2 while loops
'''n=int(input("Enter your no:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print('')
    i+=1'''
#-----------------------------------------------------------------------------
price=100000
good_credit =False
if good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment:{down_payment}")