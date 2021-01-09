print('1.Factoial using recursion.')
print('2.Fibonacci using recursion.')
print('3.Sum of series using recursion.')
print('4.Sum of list elements using recursion')
option=int(input('Enter your choice: '))
if option==1:
    def factorial(num):
        if num<2:
            return 1
        else:
            return num * factorial(num-1)

    num=int(input('Enter your number: '))
    fact=factorial(num)
    print('Factorial of number: ',fact)

elif option==2:
    def fibonacci_series(num):
        if num<=1:
            return num
        else:
            return fibonacci_series(num-1) + fibonacci_series(num-2)
    num=int(input('Enter your number: '))
    fibonacciseries=fibonacci_series(num)
    print('Fiboncci series upto nth term is: ',fibonacciseries)

    
elif option==3:
    def sumseries(num):
        for i in range(1,num+1):
            if num<=1:
                return num
            else:
                return num + sumseries(num-i)

    num=int(input('Enter your number: '))
    sum_of_series=sumseries(num)
    print('Sum of series: ',sum_of_series)

elif option==4:
    def sumlist(list):
        if len(list)==1:
            return list[0]
        else:
            return list[0] + sumlist(list[1:])
    elemnts=list(range(1,6))
    sum_of_elements=sumlist(elemnts)
    print(sum_of_elements)

else:
    print('Invalid choice.')


