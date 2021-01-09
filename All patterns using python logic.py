#STAR PATTERNS 
'''
print("1. Right Angle Triangle")
print("2. Inverted Right Angle Triangle")
print("3. 180 Degree Right Angle Triangle")
print("4. Inverted 180 Degree Right Angle Triangle")
print("5. Pyramid")
print("6. Inverted Pyramid")
print("7. Diamond")
print("8. 180 Degree Half Diamond")
print("9. 180 Degree Inverted half Diamond")

c=int(input("Enter your choice :"))
if c==1:
    print("Right Angle Triangle")
    n=int(input("Enter your number :"))
    for i in range(1,n+1):
        print(i*"*")
#---------------------------------------------------------
elif c==2:
    print("Inverted Right Angle Triangle")
    n=int(input("Enter your number :"))
    for i in range(n,0,-1):
        print(i*"*")
#---------------------------------------------------------
elif c==3:
    print("180 Degree Right Angle Triangle")
    n=int(input("Enter your number :"))
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
    print()
#---------------------------------------------------------
elif c==4:
    print(" Inverted 180 Degree Right Angle Triangle")
    n=int(input("Enter your number :"))
    for i in range(1,n+1):
        print(" "*i+"*"*(n-i))
    print()
#---------------------------------------------------------
elif c==5:
    print("Pyramid")
    n=int(input("Enter your number :"))
    for i in range(n+1):
        print(" "*(n-i)+" *"*i)
    print()
#---------------------------------------------------------
elif c==6:
    print("Inverted Pyramid")
    n=int(input("Enter your number :"))
    for i in range(n):
        print(" "*i+" *"*(n-i))
    print()
#---------------------------------------------------------
elif c==7:
    print("Diamond")
    n=int(input("Enter your number :"))
    for i in range(n):
        print(" "*(n-i-1)+" *"*(i+1))
    for i in range(n-1,0,-1):
        print(" "*(n-i)+" *"*i)
#--------------------------------------------------------
elif c==8:
    print("180 Degree Half Diamond")
    n=int(input("Enter your number :"))
    for i in range(n):
        print(i*"*")
    for i in range(n,0,-1):
        print(i*"*")
#--------------------------------------------------------
elif c==9:
    print("180 Inverted Degree Half Diamond")
    n=int(input("Enter your number :"))
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
    for i in range(1,n+1):
        print(" "*i+"*"*(n-i))
       
'''
#----------------------------------------------------------------------------------------------

#Crown Pattern
'''
*         *         *
**       * *       **
***     * * *     ***
****   * * * *   ****
***** * * * * * *****
*********************
*********************
*********************
*********************
*********************
'''
'''
n=5
for i in range(1,n+1):
    print(i*"*",end="")
    print("  "*(n-i)+" *"*i,end=" ")
    print("  "*(n-i)+"*"*i)
for i in range(1,n+1):
    for j in range(1,(22)):
        print("*",end="")
    print()
'''
#------------------------------------------------------------------
#FOX FACE
'''
      *           *
     * *         * *
    * * *       * * *
   * * * *     * * * *
  * * * * *   * * * * *
 * * * * * * * * * * * *
  * * * * * * * * * * *
   * * * * * * * * * *
    * * * * * * * * *
     * * * * * * * *
      * * * * * * *
       * * * * * *
        * * * * *
         * * * *
          * * *
           * *
            *
'''
'''
def fox(n):
    n=m-6
    for i in range(1,n+1):
        print(" "*(n-i)+" *"*i,end="")
        print("  "*(n-i),end="")
        print(" *"*i)
    for i in range(m-1,0,-1):
        print(" "*(m-i),end="")
        print(" *"*i)
    print()

m=int(input("Enter your number :"))
fox(m)
'''
#--------------------------------------------------------

#15/04/2020
'''
 * * * * * * * * * *
 * * * *     * * * *
 * * *         * * *
 * *             * *
 *                 *
 * *             * *
 * * *         * * *
 * * * *     * * * *
 * * * * * * * * * *
'''
'''
n=int(input('Enter your number : '))
for i in range(n,0,-1):
    print(i*" *",end='')
    print('    '*(n-i)+' *'*i)
for i in range(2,n+1):
    print(' *'*i,end='')
    print("    "*(n-i)+" *"*i)
'''
#---------------------------------------------------------------------------------
'''
 *                 *
 * *             * *
 * * *         * * *
 * * * *     * * * *
 * * * * * * * * * *
'''
'''
n=int(input('Enter your number : '))
for i in range(1,n+1):
    print(i*' *',end='')
    print('    '*(n-i)+' *'*i)
'''
#------------------------------------------------------------------------------------------------------
'''
 * * * * * * * * * *
 * * * *     * * * *
 * * *         * * *
 * *             * *
 *                 *
'''
'''
n=int(input('Enter your number : '))
for i in range(n,0,-1):
    print(i*" *",end='')
    print('    '*(n-i)+' *'*i)
'''
#------------------------------------------------------------------
'''
   ***** ***** 
    ***   ***
     *******
       ***
        *
'''
'''
n=int(input("Enter your number :"))
for i in range(n,0,-1):
    print(" *"*i,end='')
    print("    "*(n-i)+' *'*i)
'''
#---------------------------------------------------
############
#####--#####
####----####
###------###
##--------##
#----------#
'''
m=int(input('Enter your number: '))
n=int(input('Enter your number: '))
print('#'*m)
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print('#',end='')
    print(''*(n-i)+'-'*(2*i),end='')
    print('#'*(n+1-i)+' '*(i+1))
'''
#simple way
'''
n=int(input('Enter your number: '))
for i in range(n):
    print('#'*(n-i)+'--'*i+'#'*(n-i))
'''
#------------------------------------------------------
'''
     *
    ***
   *****
  *******
 *      *
 **    **
 ***  ***
 ********
 ***  ***
 **    **
 *      *
 *******
  *****
   ***
    *

n=int(input('Enter your number: '))
m=int(input('Enter your number: '))
for i in range(1,n-1):
    print(' '*(n-i)+(2*i-1)*'*')
for i in range(1,m+1):
    print(' '+i*"*"+'  '*(n-i-2)+'*'*i)
for i in range(m-1,0,-1):
    print(' '+i*'*',end='')
    print('  '*(m-i)+'*'*i)
for i in range(m,0,-1):
    print(' '+' '*(m-i)+'*'*(2*i-1))
'''
#---------------------------------------------------------------------------------


'''
co
com
comp
compu
comput
compute
computer

name=input('Enter your character: ')
char2=''
for char in name:
    char2+=char
    print(char2)
'''
#-----------------------------------------------------------------------------------------------
'''
* * * * * * * * * * * * * * * * * * * * * *
 *          *  *          *  *          *
  *        *    *        *    *        *
   *      *      *      *      *      *
    *    *        *    *        *    *
     *  *          *  *          *  *
      *             *             *
     *  *          *  *          *  *
    *    *        *    *        *    *
   *      *      *      *      *      *
  *        *    *        *    *        *
 *          *  *          *  *          *
* * * * * * * * * * * * * * * * * * * * * *

n=5
print('* '*(22))
for i in range(n):
    print(' '*(i+1)+'*'+'  '*(n-i)+'*',end='')
    print('  '*(i+1)+'*'+'  '*(n-i)+'*',end='')
    print('  '*(i+1)+'*'+'  '*(n-i)+'*')
print('  '*(3)+'*'+' '*(13)+'*'+' '*(13)+'*')
for i in range(n):
    print(' '*(n-i)+'*'+'  '*(i+1)+'*',end='')
    print('  '*(n-i)+'*'+'  '*(i+1)+'*',end='')
    print('  '*(n-i)+'*'+'  '*(i+1)+'*')
print('* '*(22))
'''
#-------------------------------------------------------------------------------------------------
'''
 *               *
   *           *
 *   *       *   *
   *   *   *   *
 *   *   *   *   *
   *   *   *   *
 *   *       *   *
   *           *
 *               *

for row in range(9):
    for col in range(9):
        if (row==col) or ((row==0 or row==2 or row==4 or row==6 or row==8) and (col==0 or col==8)) or ((row==1 or row==3 or row==5 or row==7)and (col==1 or col==7)) or ((row==2 or row==4 or row==6)and (col==2 or col==6)) or ((col==3 or col==5) and(row==3 or row==5)):
            print(' *',end='') 
        else:
            print(end='  ') 
    print()
'''
#simple way
'''
 *        |       *
   *      |     *
 *   *    |   *   *
   *   *  | *   *
 *   *   *|   *   *
---------------------------
   *   *   *   *
 *   *       *   *
   *           *
 *               *
'''
'''
n=5
j=n//2+1

for row in range(n-2):
    print('   * '*row)
    print('   '+'   * '*row)
print('   * '*j)
for row in range(n-3,0,-1):
    print('   '+'   * '*row)
    print('   * '*row)

print('   * '*j)
'''
#-------------------------------------------------------------------------------------------------
'''
1
4 1
9 4 1
16 9 4 1
25 16 9 4 1
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    for col in range(row,0,-1):
        print(col**2,end=' ')
    print()
'''
#--------------------------------------------------------------------------------------------------
'''
1
2 1
4 2 1
8 4 2 1
16 8 4 2 1
32 16 8 4 2 1
64 32 16 8 4 2 1
128 64 32 16 8 4 2 1
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    for col in range(row-1,-1,-1):
        print(2**col,end=' ')
    print()
'''
#--------------------------------------------------------------------------------------------------
#1
#21
#321
#4321
'''
n=int(input("Enter your number: "))
for row in range(1,n+1):
    for col in range(row,0,-1):
        print(col,end="")
    print()
'''
# or
'''
n=int(input('Enter a number: '))
for row in range(1,n+1):
    temp=row
    counter=1
    for col in range(1,row+1):
        print(temp,end=' ')
        temp-=1
        counter+=1
    print()
'''
#-----------------------------------------------------------------
'''
5 4 3 2 1 1 2 3 4 5

5 4 3 2        2 3 4 5

5 4 3               3 4 5

5 4                      4 5

5                             5

n=int(input('Enter your number: '))
for row in range(0,n):
    for col in range(n,row,-1):
        print(col,'',end='')
    for i in range(row):
        print('       ',end='')
    for j in range(row+1,n+1):
        print(j,'',end='')
    print('\n')
'''
#-----------------------------------------------------------------
#16/04/2020
'''
54321
5432
543
54
5

n=int(input('Enter a number: '))
for row in range(n+1):
    for col in range(n,row,-1):
        print(col,end='')
    print()
'''
#------------------------------------------------------------------------------------
'''
7
6 7
5 6 7
4 5 6 7
3 4 5 6 7
2 3 4 5 6 7
1 2 3 4 5 6 7
'''
'''
n=int(input('Enter your number: ')) # n=7
for row in range(n,0,-1):
    for col in range(row,n+1):
        print(col,end=' ')
    print()
'''
#--------------------------------------------------------------------
#n=int(input('Enter your number: '))
'''
a=0
b=0
for i in range(1,3):
    a+=i
    b+=a
    for j in range(a,b-i,-1):
        print(j,end=' ')
    b=0
    print()
for i in range(4,7):
    print(i,end=' ')
print()
for i in range(10,6,-1):
    print(i,end=' ')
'''
#----------------------------------------------------------------------
#27/04/2020
'''
654321
54321
4321
321
21
1
21
321
4321
54321
654321
'''
'''
n=int(input("Enter your number: "))
for row in range(n,0,-1):
    for col in range(row,0,-1):
        print(col,end='')
    print()
for row in range(1,n):
    for col in range(row+1,0,-1):
        print(col,end='')
    print()
'''
#-----------------------------------------------------------------
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
'''
n=int(input('Enter your number: '))
for row in range(n,0,-1):
    for col in range(row,0,-1):
        print(col,end=' ')
    print()
'''
#-----------------------------------------------------------------
'''
11111111
11111122
11111333
11114444
11155555
11666666
17777777
88888888
'''
'''
n=int(input('Enter your number: '))
a=1
for row in range(n-1,0,-1):
    for col in range(1,row):
        print(a,end='')
    for col in range(row,n):
        print(n-row,end='')
    print()
'''
#-------------------------------------------------
'''      
       7
      6 6
     5 5 5
    4 4 4 4
   3 3 3 3 3
  2 2 2 2 2 2
 1 1 1 1 1 1 1
'''
'''
n=int(input("Enter your number :"))
for i in range(1,n+1):
    print(' '*n,end='') 
    for j in range(i,0,-1):
        print(n,end=' ')
    n-=1
    print()
'''
#----------------------------------------------------
'''
*
12
***
1234
*****
123456
*******
12345678
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1,2):
    print('*'*row,end=' ')
    print()
    for col in range(1,row+2):
        print(col,end='')
    print()
'''
#------------------------------------------------------
'''
10000
02000
00300
00040
00005
'''
'''
n=int(input('Enter a number: '))
for row in range(1,n+1):
    print('0'*(row-1),end='')
    print(row,end='')
    print('0'*(n-row))
print()
'''
#-------------------------------------------------------------------
'''
1
10
101
1010
10101
101010
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col%2,end='')
    print()
'''
#--------------------------------------------------------------------
'''
1
121
12321
1234321
123454321
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end='')
    for col in range(row-1,0,-1):
        print(col,end='')
    print()
'''
#----------------------------------------------------------------------------
'''
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    temp=row
    counter=4
    for col in range(row):
        print(temp,end=' ')
        temp+=counter
        counter-=1
    print()
'''

#-----------------------------------------------------------------------------------
'''
1
32
654
10987
'''
'''
#Simplest Way
n=int(input('Enter your number: '))
a=0
b=0
for i in range(1,n):
    a+=i
    b+=a
    for j in range(a,b-i,-1):
        print(j,end=' ')
    b=0
    print()
'''
'''
n=int(input('Enter your number: '))
a=1
b=2
num=b
for i in range(2,n+1):
    for j in range(a,b):
        num-=1
        print(num,end=' ')
    print('')
    a=b
    b+=i
    num=b
'''
#----------------------------------------------------------------
'''
1
2 7
3 8 12
4 9 13 16
5 10 14 17 19
'''
'''
n=int(input('Enter your number: '))
for row in range(1,n+1):
    temp=row
    counter=5
    for col in range(row):
        print(temp,end=' ')
        temp+=counter
        counter-=1
    print()
'''
#----------------------------------------------------------------

'''
1
7 2
12 8 3
16 13 9 4
19 17 14 10 5
21 20 18 15 11 6
'''
'''
n=int(input('Enter your number: '))
for row in range(n): 
    for col in range(row,0,-1):
        temp=7
        counter=row
        for k in range(col):
            temp-=1
            counter+=temp
        print(counter,end=' ')
    print(row+1)
'''
'''
n = int(input('Enter your number: '))
for row in range(1,n+1):
    num = 0
    temp = row
    counter = 
    sum = 0
    lst = []
    for col in range(1,row+1):
        if temp == col:
            lst.insert(0,temp)
        else:
            sum = row + counter + num
            lst.append(sum)
            num = sum
            row = 0
            counter -= 1
    lst.reverse()
    print(*lst,end = ' ')
    print()
'''
#---------------------------------------------------------------------
'''
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''
'''
n = int(input('Enter your number: '))
min = 0  # min value of index
max= (n*2-1)-1 # max vlaue of index
temp = n
matrix =[[0 for row in range(n*2-1)] for col in range(n*2-1)]
for row in range(n):# number of iterations i.e. here 5
    for col in range(min,max+1):
        matrix[row][col]= temp
    for col in range(min+1,max+1):
        matrix[col][row] = temp
    for col in range(min+1,max+1):
        matrix[max][col] = temp
    for col in range(min+1,max+1):
        matrix[col][max] = temp
    min +=1 ; max -=1 ; temp -=1
for row in range(n*2-1):
    for col in range(n*2-1):
        print(matrix[row][col],end=' ')
    print()
'''
#---------------------------------------------------
'''
1       2       3       4       5
16      17      18      19      6
15      24      25      20      7
14      23      22      21      8
13      12      11      10      9
'''
'''
n=int(input('Eneter your number: '))
min=0
a=1 # counter to increment number 
max=n-1
iterations=(n+1)//2 # how much iterations we want
matrix=[[0 for i in range(n)] for j in range(n)] # initilize no. of rows and col
for i in range(iterations):
    for j in range(min,max+1):
        matrix[i][j]= a
        a+=1
    for j in range(min+1,max+1):
        matrix[j][max]= a
        a+=1
    for j in range(max-1,min-1,-1):
        matrix[max][j]= a
        a+=1
    for j in range(max-1,min,-1):
        matrix[j][min]= a
        a+=1
    min+=1 ; max-=1 

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end='\t')
    print()
'''