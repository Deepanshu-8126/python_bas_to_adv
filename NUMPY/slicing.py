import numpy as np
"""arr = np.array([1,2,3,4,5])
print(arr.ndim)
# print(arr.shape)
# only one element 1d array
print("First element :",arr[0])
print("Last element :",arr[-1])
"""

#2-- indexing in 2d array
"""arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("Element at row 2 and column 1 :",arr2d[2,1])
print("Element at row 3 and coumn 1 :",arr2d[2,0])
print("Element at row 1 and column 1 :",arr2d[1,0])
"""

#3-- slicing 1d arrays start stop start print sub  matrix
"""arr = np.array([10,20,30,40,50,60])
print(arr[2:6]) # 30-40
print(arr[-1:]) #only last number
print(arr[::-1]) #reverse
print(arr[:]) # all elements
print(arr[::2]) # 1 step
print(arr[0:4:2]) # one step 2
"""
# slicing 2d arrys
"""arr2d = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
print(arr2d[:,1]) #single column print"""
#sub-matrix (mix indexing + slicing0
"""arr2d = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
print(arr2d[0:2,1:3]) #sub-matrix
print(arr2d[2,:]) #last row
print(arr2d[0:2,2:])
print(arr2d[1:,1:3])"""

# Negative indexing
"""arr2d = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
print(arr2d[-1,:]) # comma lagate hi wahi end last row
print(arr2d[:,-1]) # last column
print(arr2d[::-2]) #reverse print

print(arr2d[0:3:2]) #steping 1 step
"""
# fancy indexing
"""arr=np.array([1, 2,3,4,5])
print(arr[[0,2,4]]) # index list sey select karna double round brackets"""

# Boolean indexing
"""arr=np.array([1,4,6,8,2,9])
print(arr>5) #false false true true false true

# filter values
print(arr[arr>5]) # new array create who has greater than 5"""

