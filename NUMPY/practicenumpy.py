# FILTER TOPIC
"""create a NumPy array of numbers from 1 to 50.
Filter out all even numbers.

Hint: Use modulo operator (%) with a condition inside array indexing."""
"""import numpy as np
arr=np.arange(1,51)
even=arr[arr%2==0]
print(even)#return bollean
#filter out data]

"""

# Question 2-
"""Make an array of numbers from 10 to 100 (step = 5).
Filter numbers that are greater than 50."""

"""import numpy as np
arr=np.arange(1,101,5) # 5 step gap
print(arr)
greater_than=arr[arr>50] #this will filter out data from array
print(greater_than)"""
#
# "Q3.
#
# Create a 5×5 array with values 1–25.
# Filter all numbers which are divisible by 3 but not divisible by 6.
#
# Hint: Combine two conditions using & and ~."
"""import numpy as np
arr=np.arange(1,26).reshape(5,5)
filtered_array=arr[(arr%3==0)&(arr%6!=0)]
print(filtered_array)"""

"""import numpy as np
arr=np.arange(1,26).reshape(5,5)
print(arr)
"""