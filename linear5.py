import numpy as np

A=[3,2,2,1,2,-9,-5,-10,-2,11,3,8,-1,-12,8,-16]
A=np.array(A)
reAc=np.reshape(A,(4,2,2),order='C')
print(A)