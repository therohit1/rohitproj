#Arrays.
import numpy as np
'''
a1=np.array([1,2,3,4])                           #one-dimensional array.
print(type(a1))
print(a1)

a2=np.array([[1,2,3,4],[5,6,7,8]])               #two-dimensional array
print(a2)

#Functions/Methods. - 1.Array_name=np.arrange(start,stop) 
# 2.object.reshape(no.of rows,no.of columns) 3.Array_name.shape

ar=np.arange(1,9)
print(ar)                                        #[1 2 3 4 5 6 7 8]
print(ar.shape)                                  #(8,)
print(ar.reshape(2,4))                           #2 rows , 4 columns
print(a2.shape)                                  #(2, 4)
print(a1.shape)                                  #(4,)
 
# 4.identity method- identity(n) 5.Zeros method - zeros((m,n))
print(np.identity(2))                            #[[1. 0.]
                                                 # [0. 1.]]

print(np.zeros((4,5)))
               
                                                 [[0. 0. 0. 0. 0.]
                                                  [0. 0. 0. 0. 0.]
                                                  [0. 0. 0. 0. 0.]
                                                  [0. 0. 0. 0. 0.]]
                                                  

print(np.ones((4,5)))

                                                 [[1. 1. 1. 1. 1.]
                                                 [1. 1. 1. 1. 1.]
                                                 [1. 1. 1. 1. 1.]
                                                 [1. 1. 1. 1. 1.]]


#Arithmatic operations.
print(a1*2)                                      #[2 4 6 8]
print(a1+2)                                      #[3 4 5 6]
print(a1-2)                                      #[-1  0  1  2]
print(a1//2)                                     #[0 1 1 2

print(a1+a2)                                     #[[ 2  4  6  8]
                                        #          [ 6  8 10 12]]

'''

#Accessing array elements. - 1.slicing 2.striding.
a=np.array([1,2,3,4,5])
c=np.arange(1,26).reshape(5,5)
print(a)
print(c)
'''
print(a[2])                                      #3
print(c[2,3])                                    #14
print(c[0:3:2])                                  #[[  1   2   3   4   5]
                                                #  [ 11  12  13 -14  15]]
print(c[2,0:3])                                  #[11 12 13]
print(c[3,0:4])                                  #[16 17 18 19]
#print(c[7,8])                                    #IndexError: index 7 is out of bounds for axis 0 with size 5
#print(c[1,6,11,16])                              #IndexError: too many indices for array
#print(c[6,11,16,2])                              ##IndexError: too many indices for array
'''

print(c[0:3,2])                                  #[ 3  8 13]
print(c[1,1:3])                                  #[7 8]
print(c[0:4,0])                                  #[ 1  6 11 16]
print(c[1:5,0])                                  #[ 6 11 16 21]
print(c[1:,0])                                   #[ 6 11 16 21]
print(c[1:3,2:4])                                #[[ 8  9]
                                                 #[13 14]]
print(c[::2,::2])                                #Same as below.
print(c[0:5:2,0:5:2])                            #[[ 1  3  5] only odd rows and columns.
                                              #    [11 13 15]
                                             #     [21 23 25]]
                                                 
'''

a[2]=-3
c[2,3]=-14
print(a)                                         #[ 1  2 -3  4  5]
print(c)                                         

                                                 [[  1   2   3   4   5]
                                                 [  6   7   8   9  10]
                                                 [ 11  12  13 -14  15]
                                                 [ 16  17  18  19  20]
                                                 [ 21  22  23  24  25]]

print(c[2])                                      #[ 11  12  13 -14  15]
print(c[-1])                                     #[21 22 23 24 25]
print(c[4])                         

c[-1]=[0,0,0,0,0]                                #changing last row to all zeros.
print(c)

                                                 [[  1   2   3   4   5]
                                                 [  6   7   8   9  10]
                                                 [ 11  12  13 -14  15]
                                                 [ 16  17  18  19  20]
                                                 [  0   0   0   0   0]]

'''
                                