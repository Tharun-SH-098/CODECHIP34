import numpy as np
arr1=np.array([1,2,3,4,5])
print("array 1:",arr1)
arr2=np.array([[1,2,3],[4,5,6]])
print("Array 2:\n",arr2)
print("Sum of Array 1:",np.sum(arr1))
print("Mean of Array 2:",np.mean(arr2))
print("Maximum value in  Array 1:",np.max(arr1))
print("Minimum value in Array 2:",np.min(arr2))
print("Reshaped Array 1:",arr1.reshape(5,1))
print("Transposed Array 2:\n",arr2.T)

