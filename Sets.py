#list=[1,2,1,3,4,5,2]
#Set removes duplications from the given input data
#print(set(list)) #{1,2,3,4,5}
#s={}
#print(s)
#Sets can contain numbers,strings,tuples ie immutable elements
#It cant contain mutable elements ie list,dictionaries etc
#b=[[1],1,2,3,2]                <---|
#print(set(b))


#Operations on Sets :a)Add b)Remove methods
#Add method
#f=set([1,2,3,5,8])
#p=set([2,3,5,7,11,13])
#f.add(13)#add mtd only adds the values which are not within a set)
#f.add(2)
#f.add(4)
#print(f)
#Remove method
#p.remove(13)
#p.remove(18) generates key error if element isn't present in set
#print(p)

#Use of UNION Operator(|)
#print(f|p)
#or
#print(f.union(p))

#Use of INTERSECTION Operator(&)
#print(f&p)
#or
#print(f.intersection(p))
#print(f-p)
#print(f^p)#symmetric diff :- it gives all the elements in f union p but not in f intersection p
#print(f.symmetric_difference(p))#symmetric diff :- it gives all the elements in f union p but not in f intersection p

#Checking sub sets
#a=set([1,2,3,4])
#b=set([1,2])
#print(b<=a)#gives TRUE
#print(b.issubset(a))#gives TRUE

#checking superset
#print(b>=a)#gives FALSE
#print(b.issuperset(a))#gives FALSE

#for x in a:
#    print(x)

#print(len(a))
#print(len(b))
'''print(a is b)#False
print(a is not b)#True
print(1 in a)#True
print(7 in a)#False
print(3 in b)#False'''

#Removing Duplicates from the set
marks=[20,23,22,23,20,21,23]
#print(marks)
marks_set=set(marks)
print(marks_set)
for num in marks_set:
    marks.remove(num)

duplicates=set(marks)
print(duplicates)