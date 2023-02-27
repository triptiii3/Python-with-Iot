# #to print fibonacci
# from functools import lru_cache

# @lru_cache
# def fib( n):
#     if n<=1:
#         res= n
#     else:
#         res= fib(n-1)+fib(n-2)
#         print(res)
#         return res

# n=int(input("Enter n terms: "))
import numpy as np

# arr = np.array([[1,2,3]
#                 ,[4,2,5]])
# print("array is of type: ",type(arr))

# print("No. of dimensions:",arr.ndim)

# print("Shape of array:",arr.shape)

# print("Size of array:",arr.size)

# print("Array stores element of type:",arr.dtype)

# a=np.array([[1,2,4],[5,8,7]],dtype='float')
# print("Array created using passed list: \n",a)
# b=np.array((1,3,2))
# print("Array created using tuple: \n",b)
# c=np.zeros((3,4))
# print("Array intialised with all zeroes: \n",c)

# d=np.full((3,3),6,dtype='complex')
# print("\n An array initialized with all 6s. Array type is complex:\n",d)

# e=np.random.random((2,2))
# print("\n A random array :\n",e)

# f=np.arange(0,30,5)
# print("\n A sequential array with steps of 5: \n", f)

# g=np.linspace(0,5,10)
# print("\n A sequential array with 10 values between 0 and 5: \n",g)



# arr=np.array([[1,2,3,4],
#               [5,2,4,2],
#               [1,2,0,1]])
# newarr=arr.reshape(2,2,3)

# print("\n Original Array :\n", arr)
# print("Reshaped array:\n",newarr)

# asrr=np.array([[1,2,3],[4,5,6]])
# flarr=arr.flatten()

# print("\n Original Array :\n",arr)
# print("Flattened array:\n",flarr)

arr=np.array([[-1,2,0,4],
             [4,-0.5,6,0],
             [2.6,0,7,8],
             [3 ,-7,4,2.0]])

temp=arr[:2,::2]
print("Array with first 2 rows and alternate columnes(0 and 2):\n",temp)

temp=arr[[0,1,2,3],[3,2,1,0]]
print("\n Elements at indices (0,3),(1,2),(2,1),(3,0):\n",temp)

cond=arr>0
temp=arr[cond]
print("\n Elements greater than 0:\n",cond)