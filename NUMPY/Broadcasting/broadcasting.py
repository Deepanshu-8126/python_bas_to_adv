# Broadcasting in numpy - ALlow numpy to perfomr operations on array
# definationn -- when shapes of array are diffrent numpy try to match that is called broadcasting
#Rules --
# dimension compare left to right
# if not match dimension is  1 it will expand
# otherwise error
import numpy as np
"""array1= np.array([1,2,3,4])
array2=np.array([[1],[2],[3],[4]])
print(array1.shape) # 1,4
print(array2.shape) #4,1

# broadcasting
print(array1*array2) # 4,4 matrix create
print(array1+array2) # 4,4 matrix expand
"""


"""arr = np.array([1,2,3])  # 1,3 matrix
vec=np.array([[10,20,30],  #2,3 matrix so exapnd  in 2,3 matrix format
             [4,5,6]])
print(arr+vec)
"""
# same shapes array
"""a=np.array([1,2,3])
b=np.array([10,20,30])
print(a+b)  # same shape element by element add"""

# Array + Scalar
"""a=np.array([1,2,3])
b=10
print(a+b)  # b element will add whole elements in a
"""

# 2d and 1 d ( row wise)
"""a = np.array([[1,2,3], # 2,3 matrix
             [4,5,6]])
b=np.array([10,20,30]) # 1,3 matrix
print(a+b) # expand order with 2,3 matrix

# Column wise 2d + 1d
a = np.array([[1,2,3],
             [4,5,6]])
b=np.array([[10],
            [20]])
print(a+b)  #2,3 matrix"""

