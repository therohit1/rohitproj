#n=int(input("enter your no:"))
for no in range(1,1001):    
    a=no
    c=0
    while no>0:
        rem=no%10
        c=c+pow(rem,3)
        no=no//10
    if a==c:
        print(a)
    #else:
     #   print("Not")