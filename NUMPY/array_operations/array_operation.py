# array operation and math in numpy
# we can directly use math operators in numpy array . ELEMENT - WISE
import numpy as np
#scalar arithmethic -- means singlee value
"""array = np.array([1,2,3])
print(array+1) #element wise operation har value pey
print(array*2) # all element will multiply by 2
print(array/2)
print(array-3)
print(array**5) # power of 5 every element inn array 1 powe  of 5

"""
# vector math single dimension without writing a loop
"""array=np.array([1,2,3])
#built in functions
print(np.sqrt(array))
print(np.floor(array)) #point value remove
print(np.ceil(array)) #1.0 - 2 nearest number print
"""
# combine scalar and vector
# finding area of a circle
"""radii=np.array([1,2,3])
print(np.pi*radii**2)#area of a circle = pirsquare
"""
# ELement wise arithmethic (new section)
"""array1=np.array([1,2,3,4,5])
array2=np.array([2,3,4,5,6])
print(array1+array2) # element by  element operations
print(array1*array2)"""

#COMPARSION OPERATOr
# we can  create boolean arrays , filter data , and use element wise comparison
""""scores = np.array([91,55,100,77,82,64])
print(scores==100) # retunr booleann values for every element
print(scores>=60) # return bollean who has score more than 60
#filter
scores[scores<60]=0 # assign jiske bhi 60 sey kam hey 0 assign
print(scores)
""""
