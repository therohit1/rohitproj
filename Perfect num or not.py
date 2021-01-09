n=int(input("Enter no:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
        print(n," is Perfect no !")
        exit(0)
    else:
        print("not perfect")