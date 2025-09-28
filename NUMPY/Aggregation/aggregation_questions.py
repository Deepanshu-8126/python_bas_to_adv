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

# Question 4--
# Ek 2D array (4×4) random integers (1–50) ka banao.
#
# Har row ka min aur argmin find karo.
#
# Har column ka max aur argmax find karo.
"""
import numpy as np
arr =np.random.randint(1,51,size=(4,4))
# every row min and armin
row_min = np.min(arr, axis=1)
row_argmin = np.argmin(arr, axis=1)
print(arr)
print("Row-wise Min:", row_min)
print("Row-wise Argmin:", row_argmin)

# column
col_min=np.min(arr,axis=0)
col_argmin=np.argmax(arr,axis=0)
print("Column minimum :",col_min)
print("Column wise argmax ;",col_argmin)
"""

#
# Ek 1D array banao [5, 7, 10, 15, 20, 25].
# Running sum (cumsum) aur running product (cumprod) nikaalo.
# Har step pe difference between cumsum and cumprod print karo.
"""
import numpy as np
arr=np.array([5,7,10,15,20,25])
#running summ
run_sum=np.cumsum(arr)
print(run_sum)
run_prod=np.cumprod(arr)
print(run_prod)
print(run_prod-run_sum)"""
#Ek 3D array shape (2×3×4) random integers (1–20) ka banao.
# Axis=0 par sum nikalo (yani “depth-wise collapse”).
# Axis=1 par mean nikalo (row-wise average across each block).
# Axis=2 par std nikalo (column-wise std within each row).

"""import numpy as np
arr=np.random.randint(1,21,size=(2,3,4))
# column-wise sum
print(arr)
print(np.sum(arr,axis=0))
print(np.mean(arr,axis=1))
print(np.std(arr,axis=2))"""