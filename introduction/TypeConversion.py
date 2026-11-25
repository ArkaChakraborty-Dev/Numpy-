#changing datatype

import numpy as np
arr_type=np.array([1.2,2.5,5.5])
print(arr_type.dtype)
int_arr =arr_type.astype(int)
print(int_arr.dtype)