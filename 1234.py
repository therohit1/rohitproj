n=int(input('Number: '))
for i in range(n):
    for j in range(1,i+1):
        for k in range(1,j+1):
            print('*'*k,end='')
    print()