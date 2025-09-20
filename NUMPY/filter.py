#FILTERING
import numpy as np
"""arr=np.arange(1,51)
even =arr%2==0
print(even) # condition check retunr bollean arrays
print(arr[even])  #return even number in arr to a new array
n=arr%5==0
print(n)
print(arr[n])"""
"""arr=np.random.randint(1,101,10)
#original array
print(arr)
a= arr>50
print(a)
print(arr[a]) #show number greater than 50
# less than
less_than=arr<50
print(arr[less_than])
print(less_than) #boolean return"""

# QUESTIOn
"""
arr=np.random.randint(1,101,20)
print(arr) #random integer array
#above 60
a = arr>60
print(arr[a]) #fliter
b =arr<40
print(arr[b]) # less than 40 marks filter from arr to a new array called b"""

# next question
"""arr = np.arange(1,101)
a=(arr >= 30) & (arr <= 70)
# filter values
print(arr[a]) #filter
print(a) #return bollean values
# a number which is divisible by 7 or 9
b = (arr%7==0) | (arr %9==0) #==
print(arr[b]) """

#another method
"""between_30_70 = arr[(arr >= 30) & (arr <= 70)]

# Step 3: Numbers divisible by 7 or 9
div_7_or_9 = arr[(arr % 7 == 0) | (arr % 9 == 0)]

# Output
print("Array:", arr)
print("\nNumbers between 30 and 70:\n", between_30_70)
print("\nNumbers divisible by 7 or 9:\n", div_7_or_9)"""

# Make a 5×5 matrix with numbers 1–25.
"""arr=np.arange(1,26).reshape(5,5)
print(arr) """