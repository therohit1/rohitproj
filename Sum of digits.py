n=int(input("Enter your no:"))
rem=0
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)