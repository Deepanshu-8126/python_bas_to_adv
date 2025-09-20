# INDEXING IN NUMPY IS IMPORTANT
# Ye part important hai kyunki yahi se tu arrays ke andar se specific elements nikalna,
# modify karna aur logic build karna seekhega.
# Python list jaise hi hai, but NumPy me aur powerful features hain.


# Indexing Basicsm 1-d array
"""import numpy as np
arr1=np.array([10,20,30,40,50])
print("First element :",arr1[0])  # it will print first element of arr1
print("Last element :",arr1[-1]) # negative indexing last element
"""

#INDEXING IN 2-D ARRAYS
"""import numpy as np
arr2d = np.array([[1,2,3], #3*3
                  [4,5,6],
                  [7,8,9]])
print("Element at row 0 and column 1 :",arr2d[0,1])  # row 0 -1 col 1 ==2
print("Element at row 2 and column 2 :",arr2d[2,2]) # row 3 - col 2==9
print("Element at row 1 and column 1 :", arr2d[1,1]) #5"""

# Slicing 1d arrays
"""Syntax: arr[start:end:step]
start → kaha se start
end → kaha tak (exclusive)
step → kitne step ka gap
"""

"""import numpy as np
arr = np.array([10,20,30,40,50,60]) #slicing
print(arr[0:6]) #exclusive
print(arr[:6]) # python take deault starting
print(arr[::-1]) # reverse printing
print(arr[::2]) # step 2"""

#SLICING 3D ARRAYS
import numpy  as np
arr2d = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])

# print(arr2d[0:2,1:3])

print(arr2d[:,2]) # all rows col 2
# SIngle row
print(arr2d[1,:]) # only first row
print(arr2d[:,1])  #only single column
# sub-matrix - row and column
print(arr2d[0:2,1:3])
#mix indexing +slicing
print(arr2d[1:,2:])
# negative indexing
print(arr2d[-1,:])  # last row
print(arr2d[:,-1])  # last column
print(arr2d[0:-1,-2:-1])
