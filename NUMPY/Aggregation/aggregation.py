# Aggreegate function -- Summarize data and typically return a single value
import numpy as np
array =np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
# sum all the elements use sum aggregate
print(np.sum(array)) # all elements sum return a single value
print(np.mean(array)) # mean off all - 5.5
print(np.var(array))  # variance 8.25

# .4 Min, Max, Argmin, Arg max argument
print(np.argmin(array)) # return index no  -0 minimum index zero
print(np.argmax(array)) # return index no - 9 max
print(np.min(array)) # minimum element
print(np.max(array)) # maximum element


# sum of all columns
print(np.sum(array,axis=0)) # axis =0 column wise column addition

# sum of all rows
print(np.sum(array,axis=1))

# 2d arrays axis concept axis =0 column wise axis = 1 row wise

# comparison operations
arr=np.array([10,20,30,40])
print(arr>25)
print(np.where(arr>25,1,0)) # true will assign as 1 and false will assign as false

a = np.array([1, 2, 3, 4, 5])

print(np.mean(a))    # 3.0
print(np.median(a))  # 3  middle value sorted
print(np.average(a)) # 3.0

# wieghted average
w = np.array([1, 2, 3, 4, 5])
weights = np.array([1, 1, 1, 1, 2])
print(np.average(w, weights=weights)) #3.333
# 3.67 → last element ka weight zyada

# variance and standard deviation
a = np.array([1, 2, 3, 4, 5])
print(np.var(a)) #2.0
print(np.std(a)) #1.41  sqrt 2


# range Peak to Peak = max - min
a = np.array([3, 7, 1, 9, 5])
print(np.ptp(a))  # 9-1 maximum - minimum


# cummulative frequency
# means at every step result is stores
a = np.array([1, 2, 3, 4])
print(np.cumsum(a)) # running sum
print(np.cumprod(a)) #running product [1 , 2,6,12]


