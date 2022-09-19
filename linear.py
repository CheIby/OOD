import numpy as np

A=[[7,9,-3,7],
    [9,-4,2,-8],
    [-3,2,7,-1],
    [7,-8,-1,-7]]

B=[[9,1,-4,5],
    [-7,-9,-4,2]]

A=np.array(A)
B=np.array(B)

reAc=np.reshape(A,A.T.shape,order='C')
print(reAc)
reBc=np.reshape(B,B.T.shape,order='C')
print(reBc)
reAf=np.reshape(A,A.T.shape,order='F')
print(reAf)
reBf=np.reshape(B,B.T.shape,order='F')
print(reBf)