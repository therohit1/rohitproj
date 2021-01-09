# Sum of 1st N natural numbers -
'''
n = int(input('Enter 1st N natural nos. :'))
sum = n*(n+1)//2
print(sum)
'''

# Sum of natural numbers in a given range - 
'''
n = int(input('Enter your last number from the range : '))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
'''

# Number of Handshakes in a meeting - 
'''
n = int(input('Enter number of persons : '))
Handshakes = n*(n-1)//2
print('Number of Handshakes: ',Handshakes)
'''

# Permutations in which N people can occupy M seats in a classroom - 
'''
import math
people=int(input('Enter number of people: '))
seats=int(input('Enter number of seats available: '))

if people < seats :
    temp = people
    people = seats
    seats = temp

numerator = math.factorial(people)
denominator = math.factorial((people-seats))
Permutations = numerator // denominator
print('Number of ways people can be seated : ',Permutations)
'''

# Finding HCF of Two numbers - 
'''
number1 = int(input('Enter your 1st number: '))
number2 = int(input('Enter your 2nd number: '))
for i in range(1,number1 | 1,number2):
    if (number1%i==0 & number2%i==0):
        hcf= i
print('HCF of number1 and number2: ',hcf)
'''

# Finding LCM of Two numbers -
'''
number1 = int(input('Enter your 1st number: '))
number2 = int(input('Enter your 2nd number: '))
temperary1=number1
temperary2=number2
while temperary1 != temperary2:
    if temperary1 < temperary2:
        temperary1 += number1
    else:
        temperary2+=number2
print('LCM of two numbers : ',temperary2)
'''
