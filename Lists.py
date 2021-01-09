#Getting Started With List
#creating list
'''mylist=['spam','eggs',100,1.234]
#          0      1    2    3
#         -4     -3   -2   -1
print(mylist)'''
#print(type(mylist))
#To find Length of List
#print(len(mylist))
#Use of Append and Del and Remove function to add & Delete elements from the list
#mylist.append('rohit')
#print(mylist)
#del mylist[-1]
#print(mylist)
#mylist.remove('eggs')
#print(mylist)
#removing elements from the list by index using remove functions
#k=[1,2,1,3]
#k.remove(k[2])
#print(k)
#Accesing List Elements
#print(mylist[0])
#print(mylist[-1])
#print(mylist[1:-1])#it rejects 1st and last elements and prints remaining elements

#creating list inside a list
#doublelist=['a' ,['b','c','d'],'and', 5, 6, 7, 8]
#            -7     -6         -5 -4  -3  -2 -1
#            0  [     1     ]   2   3 4 5 6
#                 0   1   2 
#               -3   -2   -1   
#print(doublelist[1])
#print(doublelist[1][0])
#print(doublelist[1][1])
#print(doublelist[1][-1])
#print(doublelist[2])
#print(doublelist[-1])
#del doublelist[2]
#print(doublelist)
#doublelist.append(9)
#doublelist.remove('a')
#print(doublelist)


#--------------------------------------------------------------------------------#


#LIST MANIPULATION:a)List slicing b)List striding c)Sorting d)Reversing e)Pop

#LIST SLICING
#primes=[2,3,5,7,11,13,17,19,23,29]
#       0 1 2 3 4  5  6  7  8  9
#      -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#print(primes[1:-1])
#print(primes[0:4])

#LIST STRIDING
#num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#print(num[1:10:2])#stepping 
#print(num[:10])
#print(num[10:])
#print(num[::2])#getting all even nos using striding method
#print(num[::3])#getting all multiples of 3

#SORTING USING SORT AND SORTED FUNCTION
#a=[1,3,5,0,8] 
#print(a)
#a.sort()
#print(a)
#print(sorted(a))

#REVERSING
#r=[1,2,3,4,5]
#r.reverse()
#print(r)
#print(r[::-1])#Reversing a list using striding method

#Sorting And Reversing common Example
#marks=[99,67,47,100,50,75,62]
#marks.sort()
#marks.reverse()
#print(marks)

#Another ways
#print(sorted(marks)[::-1])

#Popping of element
'''numbers=[5,2,1,7,4]
numbers.pop(1)#delets 2
print(numbers)'''
#--------------------------------------------
#finding greater no
'''numbers=[3,6,2,8,4,10]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)'''

#Finding smaller no
'''numbers=[3,6,2,8,4,10]
min=numbers[0]
for number in numbers:
    if number<min:
        min=number
print(min)'''

#-------------------------------------------------------
#2D lists/Matrix
'''matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#matrix[0][1]=20
#print(matrix[0][1])
#printing all the elements from the matrix
for row in matrix:
    for item in row:
        print(item)'''
#-------------------------------------------------------
#BUBBLE SORT
'''
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
print(myList)
'''
#BUBBLE SORT ON FLOATS
'''
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))
for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)
while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
print("\nSorted:")
print(myList)
'''

#Operations on lists | slices, del
myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

odds = [x for x in squares if x % 2 != 0 ]
squares = [x ** 2 for x in range(10)]
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
twos = [2 ** i for i in range(8)]
(1, 2, 4, 8, 16, 32, 64, 128)