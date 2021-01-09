#Alphabet Patterns
#P19-----A AB ABC ABCD
'''
A
A B
A B C
A B C D
A B C D E
'''
'''
n=5
for i in range(1,n+1):
    ch='A'
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
'''
#P20
'''
A B C D E
A B C D
A B C
A B
A
'''
'''
n=5
for i in range(n,0,-1):
    ch="A"
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
'''
#P21
'''
     A
    AB
   ABC
  ABCD
 ABCDE

'''
'''
n=5
for i in range(1,n+1):
    ch="A"
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)
    print()
'''
#P22
'''
ABCDE
 ABCD
  ABC
   AB
    A
'''
'''
n=5
for i in range(n,0,-1):
    ch="A"
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)
    print()
'''
#P23
'''
    A
   A B
  A B C
 A B C D
A B C D E
'''
'''
n=5
for i in range(1,n+1):
    ch="A"
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
'''

#P24
'''
A B C D E
 A B C D
  A B C
   A B
    A
'''
'''
n=5
for i in range(n,0,-1):
    ch="A"
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
'''
#------------------------------------------------------------------------------------------#
#P24-----A BC DEF GHIJ
'''
A
B C
D E F
G H I J
K L M N O
'''
'''
n=int(input("Enter your number :"))
num=65
for i in range(n):
    for j in range(i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
'''

#P25
'''
A B C D E F
G H I J K
L M N O
P Q R
S T
U
'''
'''
n=5
num=65
for i in range(n+1,0,-1):
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
'''

#P26
'''
     A
    BC
   DEF
  GHIJ
 KLMNO
'''
'''
n=5
num=65
for i in range(1,n+1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end="")
        num+=1
    print()
'''

#P27
'''
ABCDEF
 GHIJK
  LMNO
   PQR
    ST
     U
'''
'''
n=5
num=65
for i in range(n+1,0,-1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end="")
        num+=1
    print()
'''

#P28
'''
     A
    B C
   D E F
  G H I J
 K L M N O
'''
'''
n=5
num=65
for i in range(1,n+1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
'''

#P29
'''
 A B C D E
  F G H I
   J K L
    M N
     O
'''
'''
n=5
num=65
for i in range(n,0,-1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
'''
#P30
'''
     A
    B C
   D E F
  G H I J
 K L M N O
  P Q R S
   T U V
    W X
     Y
'''
'''
n=5
num=65
for i in range(1,n+1):
    print(" "*(n+1-i),end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print()
'''