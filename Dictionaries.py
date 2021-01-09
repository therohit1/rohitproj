#empty={}
#print(empty)

#Non empty dictionary 
student={'name':'rohit',
         'age' :22,
         'gender':'male',
         'class':'BE' 
}
#print(student)

#Accessing Elements
'''print(student['name'])#rohit
print(student['age'])#22
print(student['class'])#BE'''

#Add and Delete items 
#Add
#student['height']=6.2
#print(student)
 
#Delete
#del student['age']
#print(student)

#Checking key is present in a dictionary or not
#print('class' in student)
#print('age' in student)
#print(student.keys())#name age gender class
#print(student.values())#rohit 22 male BE  

#Items method
#print(student.items())#gives tuple  of key value pairs
#Displaying key value one by one
for key,value in student.items():
    print(key,value)