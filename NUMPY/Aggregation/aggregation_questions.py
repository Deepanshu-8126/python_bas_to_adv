#-- Question 1
#Ek 1D array banao 1 to 10.
# sum, mean, std, min, max find karo.
from traceback import print_tb

"""import numpy as np
arr = np.array([1,2,3,4,5])
print(np.sum(arr)) # 15
print(arr.sum()) # 15
print(arr.mean()) # 3.0
print(arr.std()) # 1.41 standard deviationn
print(np.std(arr)) # 1.41
print(np.min(arr))"""

# Ek 2D array banao (3×3).
# Row-wise aur Column-wise sum nikalo.
"""import numpy as np
arr=([[1,2,3,4,5],
      [6,7,8,9,10]])
# row wise addition
print(np.sum(arr,axis=0)) # ccolumn wise
print(np.sum(arr,axis=1)) # row wise addition
"""

#3----------Array = [10, 20, 30, 40, 50]
# np.average() use karke weighted average nikaalo jisme weights = [1, 2, 3, 4, 5].

"""import numpy as np
arr=np.array([10,20,30,40,50])
wieght = np.array([1,2,3,4,5])
mul=arr*wieght
print(mul)
add = sum(mul)
wieghts= sum(wieght)
average=add/wieghts
print(average)
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
weights = np.array([1, 2, 3, 4, 5])

w_avg = np.average(arr, weights=weights)
print("Weighted Average:", w_avg)
"""