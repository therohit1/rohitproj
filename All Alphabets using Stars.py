#A
'''
 ***
*   *
*   *
*****
*   *
*   *
*   *
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#B
'''
****
*   *
*   *
****
*   *
*   *
****
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#C
'''
****
*
*
*
*
*
****
for row in range(7):
    for col in range(5):
        if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and col>0):
            print("*",end="")
        else:
            print(end="")
    print() 
'''
#D
'''
****
*   *
*   *
*   *
*   *
*   *
****
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#E
'''
*****
*
*
*****
*
*
*****
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row ==3 or row==6) and col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#F
'''
*****
*
*
*****
*
*
*
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3) and col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#G





for row in range(7):
    for col in range(6):
        if col==0 or ((row==0 or row==6) and (col>0 and col<5)) or (row==3 and (col>2 and col<6))or (col==4 and (row==4 or row==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#H




'''
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or (row==3 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#I



'''
for row in range(7):
    for col in range(5):
        if (col==2 and (row!=0 or row!=6))or row==0 or row==6:
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#J



'''
for row in range(7):
    for col in range(5):
        if col==2 or (row==0 and col!=2) or (row==6 and col<2) or (col<1 and (row==5 or row==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#K




'''
i=0
j=4
for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1) or (row==0 and col==4) or (row==1 and col==3) or (row==2 and col==2) or (row==3 and col==1) :
            print("*",end="")
    #   elif ((row==i and col==j) and col>0):
    #        print("*",end="")
    #        i+=1
    #        j-=1
        else:
            print(end=" ")
    print()
'''
#L




'''
for row in range(7):
    for col in range(5):
        if col==0 or (row==6 and col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#M




'''
for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#N




'''
for row in range(7):
    for col in range(7):
        if col==0 or col==6 or ((row==col) and (col>0 and col<7)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#O






'''
for row in range(7):
    for col in range(5):  
        if ((col==0 or col==4) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)) :
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#P




'''
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row==1 or row==2)) or ((row==0 or row==3) and(col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#Q




'''
for row in range(8):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<6))or ((row==0 or row==6) and (col>0 and col<4)) or (row==5 and col==1) or (row==7 and col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#R







'''
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#S





'''
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6)and (col>0 and col<4)) or (col==0 and(row>0 and row<3))or (col==4 and(row>3 and row<6)) :
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#T






'''
for row in range(5):
    for col in range(5):
        if row==0 or (col==2 and row>0):#col==2 and(row==0 and col!=2)
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#U






'''
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and row!=6) or (row==6 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#V






'''
i=0
j=6
for row in range(4):
    for col in range(7 ):
        if row==col :
            print("*",end="")
        elif row==i and col==j:
            print("*",end="")
            i+=1
            j-=1
        else:
            print(end=" ")
    print()
'''
#W









'''
i=0
j=3
for row in range(4):
    for col in range(7):
        if col==0 or col==6 or (col==5 and row==2) or (col==4 and row==1):
            print("*",end="")
        elif row==i and col==j:
            print("*",end="")
            i+=1
            j-=1
        else:
            print(end=" ")
    print()
'''
#X









'''
i=0
j=4
for row in range(5):
    for col in range(5):
        if  row==i and col==j:
            print("*",end="")
            i+=1
            j-=1
        elif row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#Y






'''
for row in range(5):
    for col in range(5):
        if (col==2 and row>1) or(row==col and row<2): 
            print("*",end="")
        elif (row==0 and col==4)or(row==1 and col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#Z






'''
i=1
j=4
for row in range(6):
    for col in range(6):
        if row==0 or row==5:
            print("*",end="")
        elif row==i and col==j:
            print("*",end="")
            i+=1
            j-=1
        else:
            print(end=" ")
    print()
'''















#----------------------------------------------------------------------------------------------------------
#ROHIT
'''
for row in range(5):
    for col in range(27):
        if row==0 and col in{0,1,2,6,7,10,14,16,17,18,19,20,22,23,24,25,26}:
            print("*",end=" ")
        elif row==1 and col in{0,3,5,8,10,14,18,24}:
            print("*",end=" ")
        elif row==2 and col in{0,1,2,5,8,10,11,12,13,14,18,24}:
            print("*",end=" ")
        elif row==3 and col in{0,1,5,8,10,14,18,24}:
            print("*",end=" ")
        elif row==4 and col in{0,2,6,7,10,14,16,17,18,19,20,24}:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''
for row in range(10):
    for col in range(11):
        if row==0 and col in{2,3,7,8}:
            print("*",end=" ")
        elif row==1 and col in{1,4,6,9}:
            print("*",end=" ")
        elif row==2 and col in{0,5,10}:
            print("*",end=" ")
        elif row==3 and col in{0,10}:
            print("*",end=" ")
        elif row==4 and col in{0,10}:
            print("*",end=" ")
        elif row==5 and col in{1,9}:
            print("*",end=" ")
        elif row==6 and col in{2,8}:
            print("*",end=" ")
        elif row==7 and col in{3,7}:
            print("*",end=" ")
        elif row==8 and col in{4,6}:
            print("*",end=" ")
        elif row==9 and col==5:
            print("*",end=" ")       
        else:
            print(" ",end=" ")
    print()
'''