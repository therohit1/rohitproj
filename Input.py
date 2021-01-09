a=int(input("Enter your no:"))
#if n>0:
#    print("Positive no.")
#    exit(0)
#print("Negative no.")
b=int(input("Enter your no:"))
c=int(input("Enter your no:"))
if (a>b and a>c):
    print("a is greater")
    exit(0)
elif b>a and b>c:
    print("b is greater")
    exit(0)
elif c>a and c>b:
    print("c ia greater")
    exit(0)
else:
    print("All are equal")