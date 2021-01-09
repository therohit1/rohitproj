# Sorting in Ascending value
list1=[56,3,2,78,6,0]
for i in range(len(list1)):
    min_value=min(list1[i:])
    min_ind=list1.index(min_value)
    list1[i],list1[min_ind]=list1[min_ind],list1[i] #swapping min value with max value
print(list1)