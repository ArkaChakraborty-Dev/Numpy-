'''
Slicing

array[start:stop:step]
'''

import numpy as np

arr=np.array([10,20,30,40,50,60])

print(arr[1:5:1]) #index 1 to 4
print(arr[:4]) #iindex 0 to 3
print(arr[::2]) #every second element
print(arr[::-1]) #Reverse the array