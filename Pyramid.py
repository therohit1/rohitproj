#n=int(input("Enter your no:"))
'''for i in range(1,5):
    for j in range(4,i-1,-1):
        print(" ",end=" ")
        print("*",end=" ")
    print()
'''
#ALternate way
n=5
for rows in range(n):
    print(" "*(n-rows-1),"* "*(rows+1))
for rows in range(n-1,0,-1):
    print(" "*(n-rows),"* "*(rows))

'''
1
2 3
4 5 6
7 8 9 10
'''
