#Using Flag

for i in range(1,101):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2: # 2 factors beacause prime number has only 2 factors.
        print(i,end=' ')
print("\n")


