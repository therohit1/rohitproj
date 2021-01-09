#NUMBER PATTERNS :
#P1-----1 12 123 1234
'''
1
12
123
1234
12345
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
'''

#P2
'''
12345
1234
123
12
1
'''
'''
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

#P3
'''
     1
    12
   123
  1234
 12345
'''
'''
n=5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

#P4
'''
 12345
  1234
   123
    12
     1
'''
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

#P5
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''
'''
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#P6
'''
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
'''
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''

#--------------------------------------------------------------
#P7-----1 22 333 4444 
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
#P8
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
'''
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
#P9
'''
    1
   22
  333
 4444
55555
'''
'''
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
'''
#P10
'''
55555
 4444
  333
   22
    1
'''
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
'''
#P11
'''
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
'''
'''
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
#P12
'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
'''
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
#---------------------------------------------------------
#P13-----1 23 456 789 
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
'''
n=5
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print()

'''
#P14
'''
1 2 3 4 5
6 7 8 9
10 11 12
13 14
15
'''
'''
n=5
a=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print()
'''
#P15 
'''
   1
  23
 456
78910
'''
'''
n=4
a=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    print()
'''
#P16
'''
 123
  45
   6
'''
'''
n=3
a=1
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    print()
'''
#P17
'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
'''
n=5
a=1
for i in range(1,n):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print()
'''
#P18
'''
1 2 3 4
 5 6 7
  8 9
   10
'''
'''
n=5
a=1
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(a,end=" ")
        a+=1
    print()
'''