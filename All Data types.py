#Data types - 
'''
1.Strings.
2.Lists.
3.Tuples.
4.Sets.
5.Dictionaries.
'''

#strings - collection of characters placed inside (' '/'' ''/'''  ''') which can't be modified after its creation(Immutable).
#Built in Functions -
''' 
 1.string_name.find(parameter) 
 2.string_name.capitilize() 
 3.string_name.upper() 
 4.string_name.lower() 
 5.string_name.replace(para1,para2)
 6.string_name1.join(string_name2) 
 7.string_name.count(parameter) 
 8.string_name.split()
 9.string_name.startswith(parameter)
 10.string_name.endswith(parameter)
'''
'''
s='hello World!'

print(type(s))
print(s[0])                                       #h
print(s[-1])                                      #!
print(s[:5])                                      #hello
print(s[1:])                                      #ello World!
print(s[1:-1])                                    #ello World
print(s[::-1])                                    #!dlroW olleh
name='Rohit waghmare'
print(name[-4:-1])                               #mar
print(name[-4::-1])                              #mhgaw tihoR 


print(s.find('o'))                                #4
print(s.find('l'))                                #2

print(s.capitalize())                             #Hello world!

print(s.upper())                                  #HELLO WORLD!
print(s.lower())                                  #hello world!

print(s.replace('l','L'))                         #heLLo WorLd!
print('-'.join(s))                                #h-e-l-l-o- -W-o-r-l-d-!
print(s.count('l'))                               #3

print(s.startswith('he'))                        #True
print(s.startswith('He'))                        #False
print(s.endswith('d!'))                          #True
print(s.endswith('D!'))                          #False



str='line1-abcdef \n line2-abc \n line3-abcd'
print(str.split())                                #['line1-abcdef', 'line2-abc', 'line3-abcd']

#Examples-
email='mr[dot]waghmarerohit[at]gmail[dot]com'
email1=email.replace('[dot]','.')
print(email1)
print(email1.replace('[at]','@'))

#Check the input string if its contain any vowel then Print the string without including vowels.
str='Rohit Waghmare'
str=str.upper()
for char in str:
    if char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        continue
    print(char)                                  #RHT WGHMR

#or
name='Rohit Waghmare'
name=name.upper()
new=name
vowels=('A','E','I','O','U')
for r in name:
    for r in vowels:
        new=new.replace(r,'')
print(new)                                       #RHT WGHMR

#String Formatting.
fname='Rohit'
lname='Waghmare'
print(f'{fname} {lname} is a coder.')            #Rohit Waghmare is a coder.

#Removing Dots from the string.
str='F.R.I.E.N.D.S'
print(str[::2])                                  #FRIENDS

'''

#--------------------------------------------------------------------------------------------------

#Lists - It's a data structure which can collect and store sequence of elements which need not be of same data types.It's mutable data structure.
#Creating list by taking input from the user
'''
list1=[]
num=int(input('How many numbers you want to enter: '))
print('Enter the values: ')
for i in range(num):
    list1.append(int(input()))
print(list1)
'''
#Built in Functions -
'''
 1.list_name.append(paramter)
 2.list_name.remove(parameter)
 3.list_name.pop(parameter) 
 4.list_name.sort() / sorted(list_name) 
 5.list_name.reverse()
 6.del(parameter)
 7.list_name1.extend(list_name2) 
 8.list_name1.copy(list_name2) 
 9.list_name.insert(index,parameter)
 10.list_name.index(parameter)
 11.list_name.clear()
'''
'''
myList=['Rohit',1,1.2,'Waghmare']
print(type(myList))                              #<class 'list'>
print(myList[0])                                 #Rohit
print(myList[-1])                                #Waghmare
print(myList[1:-1])                              #[1, 1.2]

myList.append(5)
print(myList)                                    #['Rohit', 1, 1.2, 'Waghmare', 5]

myList.remove(5)
print(myList)                                    #['Rohit', 1, 1.2, 'Waghmare']

myList.remove(myList[1])
print(myList)                                    #['Rohit', 1.2, 'Waghmare'] Removing by Index.

myList.insert(4,10)
print(myList)                                    #['Rohit', 1.2, 'Waghmare', 10]

num1=[1,3,2,5,4]
num1.pop(0)                                      #[3, 2, 5, 4]
print(num1)

num1.sort()                                      #[1, 2, 3, 4, 5]
print(num1)

print(sorted(num1))                              #[1, 2, 3, 4, 5]      

num1.reverse()                                   #[5, 4, 3, 2, 1]
print(num1) 

#Creating List inside a List.

doublelst=[1,2,3,[4,5,6],7,8]                    #2
print(doublelst[1])
print(doublelst[3])                              #[4, 5, 6]
print(doublelst[3][1])                           #5

print(doublelst.index(2))                        #1

doublelst.clear()
print(doublelst)                                 #[]

#Shortcut to create Lists of n range.
print(list(range(1,10,2)))                       #[1, 3, 5, 7, 9] List of odd numbers.

#or print(num[::2])
print(list(range(0,10,2)))                       #[0, 2, 4, 6, 8] List of even numbers.

num=(list(range(1,10)))                          #[1, 2, 3, 4, 5, 6, 7, 8, 9] Creates a list.This is shortcut of creating a list.
print(num)
print(num[1:])                                   #[2, 3, 4, 5, 6, 7, 8]
print(num[:-1])                                  #[1, 2, 3, 4, 5, 6, 7, 8]
print(num[::2])

a=list(range(1,6))
del(a)
print(a)

a=list(range(1,6))                               #[1, 2, 3, 4, 5]
b=list(range(6,11))                              #[6, 7, 8, 9, 10]
a.extend(b)
print(a)                                         #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a=list(range(1,6))                               #[1, 2, 3, 4, 5]
b=a.copy()    
print(b)                                         #[1, 2, 3, 4, 5]

num=[1,2,3,4,5]
print(sum(num))                                  #15
print(min(num))                                  #1
print(max(num))                                  #5

#Merge 2 lists into dictionary.
name=['rohit','akshay']
num=[1,2]
dic=dict(zip(name,num))
print(dic)                                       #{'rohit': 1, 'akshay': 2}

#Examples -
#Finding Maximum number from a list.
numbers=list(range(1,10))
print(numbers)
max=numbers[0]
for num in numbers:
    if num>max:
        max=num
print(max)                                       #9

#Finding Minimum number from a list.
numbers=list(range(1,10))
print(numbers)
min=numbers[0]
for num in numbers:
    if num<min:
        min=num
print(min)                                       #1
       
#Removing Duplications from List.
numbers=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)                                    #[1, 2, 3, 4, 5]


numbers=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
a=set(numbers)                                   #{1,2,3,4,5}
print(list(a))                                   #[1, 2, 3, 4, 5]
'''
#--------------------------------------------------------------------------------------------------

#Tuples - It's a data structure which can collect and store the elements which need to be of same data type.(Immutable).
#Built in Functions - 
'''
 1.tuple_name.count(parameter) 
 2.tuple_name.index(parameter)
'''
'''
t=(1,-1,1.2,'Hello',-2,-1,5,1.4)
print(type(t))                                   #<class 'tuple'>
print(t[1])                                      #-1
print(t[-1])                                     #1.4
print(t[:3])                                     #(1, -1, 1.2)
print(t[::-1])                                   #(1.4, 5, -1, -2, 'Hello', 1.2, -1, 1)
print(t[1:-1])                                   #(-1, 1.2, 'Hello', -2, -1, 5)
print(t[2:])                                     #(1.2, 'Hello', -2, -1, 5, 1.4)
print(t[1:8])                                    #(-1, 1.2, 'Hello', -2, -1, 5, 1.4) in steps of two

print(t.count(-1))                               #2 
print(t.index('Hello'))                          #3

#Example - 
# Unpacking
coordinates=(1,2,3)
x=coordinates[0]                                #1
y=coordinates[1]                                #2
z=coordinates[2]                                #3
#or
x,y,z=coordinates
print(x)
print(y)
print(z)

'''

#--------------------------------------------------------------------------------------------------
#Sets - It's unoredered collection of unique elements  ie.only contains unique elements by removing the duplications.(Mutable). 
# Built in Functions - 
'''
 1.set_name.add(parameter) 
 2.set_name.remove(parameter) 
 3.set_name1.union(set_name2) 
 4.set_name1.intersection(set_name2) 
 5.set_name1.difference(set_name2) 
 6.set_name1.symmetric difference((set_name2)   
 7.set_name1.issubset(set_name2)   
 8.set_name1.issuperset(set_name2) 
 9.set_name1.isdisjoint(set_name2) 
'''
'''
s=set(range(1,6))                                #{1, 2, 3, 4, 5}
print(s)

a=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print(set(a))                                    #{1, 2, 3, 4, 5}
print(len(set(a)))                               #5

for x in set(a):
    print(x,end='')                              #12345

b=set([1,2,3,4,5])
print(b)                                         #{1, 2, 3, 4, 5}
b.add(6)
print(b)                                         #{1, 2, 3, 4, 5, 6}

c=set([6,7,8,9,10])                              #{6, 7, 8, 9, 10}
print(c)

c.remove(10)
print(c)                                         #{6, 7, 8, 9}

print(b|c)                                      #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(b&c)                                      #{6}

f={1,2,3,5,8,13}
p={2,3,5,7,11}
print(f.union(p))                                #{1, 2, 3, 5, 7, 8, 11, 13}

print(f.intersection(p))                         #{2, 3, 5}

print(f.difference(p))                           #{8, 1, 13}

print(f.symmetric_difference(p))                 #{1, 7, 8, 11, 13}

print(f.issuperset(p))                           #False

print(f.isdisjoint(p))                           #False

print(f.issubset(p))                             #False

#Example - list all the duplicates from a given list using sets.
marks=[20,23,22,23,20,21,23]
marks_set=set(marks)                             #{20, 21, 22, 23}
for num in marks_set:
    marks.remove(num)
duplicates=set(marks)
print(duplicates)                                #{20, 23}        

'''

#--------------------------------------------------------------------------------------------------
#Dictionaries - It's an unordered collection of items which has key:value pair. Keys are unique but values may differ(can be of different data types)
# Mutable.
#Built in Functions - 
'''
 1.del dictionary_name(parameter) 
 2.dictionary_name.keys() 
 3.dictionary_name.values()
 4.dictionary_name.items()
 5.dictionary_name.get(paramter)
'''
'''
dict={}
print(dict)                                      #{} empty dictionary.

student={ 'name':'rohit',
          'age':22,
          'gender':'male',
          'class':'BE'  
        }
print(student)                                   #{'name': 'rohit', 'age': 22, 'gender': 'male', 'class': 'BE'}

print(student['name'])                           #rohit

print(student.get('name'))                       #rohit
print(student['age'])                            #22

student['height']=6.2
print(student)                                   #{'name': 'rohit', 'age': 22, 'gender': 'male', 'class': 'BE', 'height': 6.2}

student['class']=12
print(student)                                   #{'name': 'rohit', 'age': 22, 'gender': 'male', 'class': 12, 'height': 6.2}

del(student['age'])
print(student)                                   #{'name': 'rohit', 'gender': 'male', 'class': 12, 'height': 6.2}


print('school' in student)                       #False
print('name' in student)                         #True

print(student.keys())                            #dict_keys(['name', 'gender', 'class', 'height'])
print(student.values())                          #dict_values(['rohit', 'male', 12, 6.2])
print(student.items())                           #dict_items([('name', 'rohit'), ('gender', 'male'), ('class', 12), ('height', 6.2)])

#Examples- mapping characters into numbers.
phone=input('Phone: ')
digits_mapping={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '10':'ten'
}
output=''
for ch in phone:
    output+=digits_mapping.get(ch)+' '
print(output)

'''

#--------------------------------------------------------------------------------------------------
#Arrays - It's a homogeneous data structure which collects and store elements of same data types.(Mutable). 
#Built in Functions - 
'''
 1.Array_name=np.arrange(start,stop) 
 2.Array_name.reshape(no.of rows,no.of columns) 
 3.Array_name.shape
 4.identity method- Array_name.identity(n) 
 5.Zeros method - Array_name.zeros((m,n))
 6.Ones method -  Array_name.ones((m,n))

'''
'''
import numpy as np

a1=np.array([1,2,3,4])                           #one-dimensional array.
print(type(a1))
print(a1)

a2=np.array([[1,2,3,4],[5,6,7,8]])               #two-dimensional array.
print(a2)

#Functions/Methods. - 
ar=np.arange(1,9)
print(ar)                                        #[1 2 3 4 5 6 7 8]

print(ar.shape)                                  #(8,)
print(ar.reshape(2,4))                           #2 rows , 4 columns
print(a2.shape)                                  #(2, 4)
print(a1.shape)                                  #(4,)
 

print(np.identity(2))                            #[[1. 0.]
                                                 # [0. 1.]]

print(np.zeros((4,5)))
               
                                                 #[[0. 0. 0. 0. 0.]
                                                 # [0. 0. 0. 0. 0.]
                                                 # [0. 0. 0. 0. 0.]
                                                 # [0. 0. 0. 0. 0.]]
                                                  

print(np.ones((4,5)))

                                                 #[[1. 1. 1. 1. 1.]
                                                 # [1. 1. 1. 1. 1.]
                                                 # [1. 1. 1. 1. 1.]
                                                 # [1. 1. 1. 1. 1.]]


#Arithmatic operations.
print(a1*2)                                      #[2 4 6 8]
print(a1+2)                                      #[3 4 5 6]
print(a1-2)                                      #[-1  0  1  2]
print(a1//2)                                     #[0 1 1 2

print(a1+a2)                                     #[[ 2  4  6  8]
                                                 # [ 6  8 10 12]]



#Accessing array elements. - 1.slicing 2.striding.
a=np.array([1,2,3,4,5])
c=np.arange(1,26).reshape(5,5)
print(a)
print(c)

print(a[2])                                      #3
print(c[2,3])                                    #14
print(c[0:3:2])                                  #[[  1   2   3   4   5]
                                                 # [ 11  12  13 -14  15]]

print(c[2,0:3])                                  #[11 12 13]
print(c[3,0:4])                                  #[16 17 18 19]
#print(c[7,8])                                    #IndexError: index 7 is out of bounds for axis 0 with size 5
#print(c[1,6,11,16])                              #IndexError: too many indices for array
#print(c[6,11,16,2])                              #IndexError: too many indices for array


print(c[0:3,2])                                  #[ 3  8 13]
print(c[1,1:3])                                  #[7 8]
print(c[0:4,0])                                  #[ 1  6 11 16]
print(c[1:5,0])                                  #[ 6 11 16 21]
print(c[1:,0])                                   #[ 6 11 16 21]

print(c[1:3,2:4])                                #[[ 8  9]
                                                 #[13 14]]
                                                 
print(c[::2,::2])                                #Same as below.
print(c[0:5:2,0:5:2])                            #[[ 1  3  5] only odd rows and columns.
                                                 # [11 13 15]
                                                 # [21 23 25]]
                                                 


a[2]=-3
c[2,3]=-14
print(a)                                         #[ 1  2 -3  4  5]
print(c)                                         

                                                 #[[  1   2   3   4   5]
                                                 # [  6   7   8   9  10]
                                                 # [ 11  12  13 -14  15]
                                                 # [ 16  17  18  19  20]
                                                 # [ 21  22  23  24  25]]

print(c[2])                                      #[ 11  12  13 -14  15]
print(c[-1])                                     #[21 22 23 24 25]
print(c[4])                         

c[-1]=[0,0,0,0,0]                                #changing last row to all zeros.
print(c)

                                                 #[[  1   2   3   4   5]
                                                 # [  6   7   8   9  10]
                                                 # [ 11  12  13 -14  15]
                                                 # [ 16  17  18  19  20]
                                                 # [  0   0   0   0   0]]

'''

#------------------------------------------------END------------------------------------------------                           

























