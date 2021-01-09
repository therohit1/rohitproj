# Sorting in Ascending order
'''
list1 = [10,15,4,23,0]
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j] #Swapping 
           #temp = list1[j]
           #list1[j] = list1[j+1]
           #list1[j+1] = temp
        print('Iterations : ',list1,'\n')
print('Sorted list: ',list1) 

'''
'''
Iterations :  [10, 15, 4, 23, 0]

Iterations :  [10, 4, 15, 23, 0]

Iterations :  [10, 4, 15, 23, 0]

Iterations :  [10, 4, 15, 0, 23]

Iterations :  [4, 10, 15, 0, 23]

Iterations :  [4, 10, 15, 0, 23]

Iterations :  [4, 10, 0, 15, 23]

Iterations :  [4, 10, 0, 15, 23]

Iterations :  [4, 10, 0, 15, 23]

Iterations :  [4, 0, 10, 15, 23]

Iterations :  [4, 0, 10, 15, 23]

Iterations :  [4, 0, 10, 15, 23]

Iterations :  [0, 4, 10, 15, 23]

Iterations :  [0, 4, 10, 15, 23]

Iterations :  [0, 4, 10, 15, 23]

Iterations :  [0, 4, 10, 15, 23]

Sorted list:  [0, 4, 10, 15, 23]
'''
'''
#Sorting in Descending order
list2 = [10,15,4,23,0]
for i in range(len(list2)-1):
    for j in range(len(list2)-1):
        if list2[j] < list2[j+1]:
            list2[j],list2[j+1]=list2[j+1],list2[j] #Swapping
           #temp = list2[j]
           #list2[] = list2[j+1]
           # list2[j+1] = temp
        print('Interations : ',list2,'\n')
print('Sorted list : ',list2)  

'''
'''
Interations :  [15, 10, 4, 23, 0]

Interations :  [15, 10, 4, 23, 0]

Interations :  [15, 10, 23, 4, 0]

Interations :  [15, 10, 23, 4, 0]

Interations :  [15, 10, 23, 4, 0]

Interations :  [15, 23, 10, 4, 0]

Interations :  [15, 23, 10, 4, 0]

Interations :  [15, 23, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Interations :  [23, 15, 10, 4, 0]

Sorted list :  [23, 15, 10, 4, 0]
'''

#Another Way
'''
list1 = [10,15,4,23,0]
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j] #Swapping
            print(list1)
print('Sorted List',list1)

'''

#Another way
'''
list1 = [10,15,4,23,0]
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j] #Swapping
            print(list1)
        else:
            print(list1)
    print()
print('Sorted List',list1)

'''
'''
[10, 15, 4, 23, 0]
[10, 4, 15, 23, 0]
[10, 4, 15, 23, 0]
[10, 4, 15, 0, 23]

[4, 10, 15, 0, 23]
[4, 10, 15, 0, 23]
[4, 10, 0, 15, 23]

[4, 10, 0, 15, 23]
[4, 0, 10, 15, 23]

[0, 4, 10, 15, 23]

Sorted List [0, 4, 10, 15, 23]
'''

#Another way
'''
list1 = [10,15,4,23,0]
for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j] #Swapping
            print(list1)
        else:
            print(list1)
    print()
print('Sorted List',list1)

'''
'''
[10, 15, 4, 23, 0]
[10, 4, 15, 23, 0]
[10, 4, 15, 23, 0]
[10, 4, 15, 0, 23]

[4, 10, 15, 0, 23]
[4, 10, 15, 0, 23]
[4, 10, 0, 15, 23]

[4, 10, 0, 15, 23]
[4, 0, 10, 15, 23]

[0, 4, 10, 15, 23]

Sorted List [0, 4, 10, 15, 23]
'''