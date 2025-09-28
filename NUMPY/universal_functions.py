# in numpy there are many built in  multidimensions function that apply fast in all element
from cgi import print_environ_usage

import numpy as np
arr = np.array([1,4,9,16])
print("Sqaure root ",np.sqrt(arr)) # 1 2 3 4
print("Exponential ",np.exp(arr))
print("Logarithm ",np.log(arr))


# Trignomentric functions
angles = np.array([0,np.pi/2,np.pi])
print("sin" ,np.sin(angles))
print("cos",np.cos(angles))
print("tan",np.tan(angles))

# Rounding Functions
np.round(arr)
np.floor(arr)
np.ceil(arr)