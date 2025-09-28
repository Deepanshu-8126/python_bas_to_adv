# Array atrributes in Numpy
# Create a 2d array
"""import numpy as np
arr = np.array([[1,2,3] ,[4,5,6]])
print(arr) # yey hamne 2d matrix bana di aab attributes dekhenge
# shape
print("SHAPE:",arr.shape) # it will give kitne by kitne ki matrix hey rows and columns
# Dimension
print(arr.ndim) # 2 dimension 2d
#Size --- total elements
print(arr.size) # 6
# Data type
print(arr.dtype) #int64"""

# 4. Different Data Types
#
# NumPy arrays ek hi type ke hote hain (lists me mixed types ho sakte hai).
"""import numpy as np
arr_int = np.array([1,2,3], dtype='int32')
arr_float = np.array([1,2,3], dtype='float64')

print("Integer array:", arr_int)
print("Float array:", arr_float)"""
#------------------------------------------------------------------------------------------------------------
# Practice questions
#1--Ek NumPy array banao from list [2,4,6,8,10].
"""import numpy as np
arr1=[2,4,6,8,10]
print(arr1)
#another method range
np.arange(2,10,1)
print(arr1)  # it will also work
"""
#2--4x4 ka zero matrix banao.
"""import numpy as np
zeroes=np.zeros((4,4))
print(zeroes)"""
#3--1–15 tak ke numbers ka array banao with step=3.
"""import numpy as np
arr=np.arange(1,15,3)
print(arr)"""
#4--Shape, size aur dimensions print karo ek 3x2 ones matrix ke.
"""import numpy as np
arr=np.ones((3,2))
print("Shape",arr)
print("Dimensions:",arr.ndim)"""

#5--5 equally spaced numbers banao between 50 and 100.
"""import numpy as np
arr=np.linspace(50,100,5)
print(arr)"""

