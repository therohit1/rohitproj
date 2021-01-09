#Progarm 1 - list comprehension

def f(x):
    return x**2
#creating a list of squares
data=[f(x) for x in range(11)]
#print content of data 
for x in range(1,11):
    print(f'{x}={data[x]}')  

#Program 2 - Find the average value
'''
data=[10,20,30,40,50]
avg=sum(data)/len(data)
print(avg)
'''
#Program 3 - Find statistical mean using library function
'''
import statistics
data=[10,20,30,40,50]
avg=statistics.mean(data)
print(avg)
'''
#Program 4 - Find statistical median
'''
import statistics
data=[1,2,10,20,100]
print(statistics.median(data))
data2=[1,2,10,20,100,200]
print(statistics.median(data2))
'''
#Program 5 - Bubble sort
'''
data=[4,7,1,4,8,9,3,2,5,6]
done=0
while not done:
    done=1
    for n in range(1,len(data)):
        if data[n-1]>data[n]:
            data[n-1],data[n]=data[n],data[n-1]
            done=0 #Continue
print(data)
'''
#Program 6 - Reversing a number
'''
n=int(input('Enter your number: '))
r=int(str(n)[::-1])
print(r)
'''
#Program 7 - To check whether  given year is leap using library function
'''
import calendar
year=int(input('Enter a year: '))
is_leap=calendar.isleap(year)
print(is_leap)
'''
#Program 8 - Computing a factorial using library function
'''
import math
for i in range(1,11):
    f=math.factorial(i)
    print(f'{i}!={f}')
'''