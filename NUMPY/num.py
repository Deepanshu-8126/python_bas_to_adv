# #  Basic numpy
# 1. NumPy Kya Hai?
# 👉 NumPy (Numerical Python) ek Python library
# hai jo mainly mathematical operations & arrays ke liye use hoti hai.
# Python me normal list bhi hoti hai, lekin list
# slow hoti hai aur usme large data pe operations easy nahi hote.
# NumPy array fast hoti hai aur matrix / mathematical operations easily support karti hai.


"""import numpy as np
# normal list
list1=[1,2,3,4,5]

# numpy array
arr=np.array([1,2,3,4,5])
print("PYthon list ",list1)
print("Numpy Array :", arr)
"""

# ➡️ Dono same lagte hai, lekin difference ye hai ki NumPy arrays ke
# andar mathematical operations directly ho jaate hain.

# Creating array (Array Creation)
# 1-- Method python list
"""import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
"""
#2-- Method --Zeroes and ones zero and one matrix
"""import numpy as np
zeroes =np.zeros((2,3)) # 2 by 3 matriz 2 rows 3 columns
print(zeroes)
ones = np.ones((4,3)) # 4 by 3 matrix 
print(ones)

"""
# 3-- Full array with all values with same number
"""import numpy as np
full = np.full((2,2),7)
print(full) """

# 4-- Range of numbers like in python we give start stop step usinf np.arange
"""import numpy as np
arr=np.arange(1,10,2)
print(arr)"""

#5-- Evenly spaced numbers -- start to end number ke beech ke numbers step mey utne numbers
"""import numpy as np
arr1=np.linspace(1,5,6)
print(arr1)

"""
#6--(f) Identity Matrix diagonal elements 1 baki 0
"""import numpy as  np

identity = np.eye(3)   # 3x3 identity matrix
print(identity)
"""


#_----------------
# create an array  from 1 to 50
"""import numpy as  np
arr=np.arange(1,101) # array creation round bracket only
print(arr.shape)
print(arr)
arr_reshape=arr.reshape(10,10)
print(arr_reshape.shape) #10,10 ka shape hogya aab
# find the 50th element
print(f"50 th element is {arr[49]}")
# reverse the array
print(arr[::-1]) # negaive indexing step -1 sey peecche jana hey 
"""
