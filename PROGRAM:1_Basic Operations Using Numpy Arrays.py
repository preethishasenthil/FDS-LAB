Get the data type of an array object
PROGRAM:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
OUTPUT:
int64
Get the data type of an array containing strings
PROGRAM:
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
OUTPUT:
<U6
Create an array with data type string
PROGRAM:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
OUTPUT:
[b'1' b'2' b'3' b'4']
|S1
Create an array with data type 4 bytes integer
PROGRAM:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
OUTPUT:
[1 2 3 4]
int32
Change data type from float to integer by using 'i' as parameter value
PROGRAM:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
OUTPUT:
[1 2 3]
int32
Change data type from float to integer by using int as parameter value
PROGRAM:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
OUTPUT:
[1 2 3]
int64
Change data type from integer to boolean
PROGRAM:
import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
OUTPUT:
[ True False True]
bool
demonstrate the working of array()
PROGRAM:
import array
arr = array.array('i', [1, 2, 3])
print ("The new created array is : ",end="")
for i in range (0,3):
print (arr[i], end=" ")
print ("\r")
OUTPUT:
The new created
array is : 1 2 3
Intrinsic Numpy Array Creation
PROGRAM:
import numpy as np
arr=np.arange(10)
print(arr)
OUTPUT:
[0 1 2 3 4 5 6 7 8 9]
PROGRAM:
import numpy as np
arr=np.arange(2, 10, dtype=np.float)
print(arr)
OUTPUT:
[2. 3. 4. 5. 6. 7. 8. 9.]
PROGRAM:
import numpy as np
arr=np.arange(2, 3, 0.1)
print(arr)
OUTPUT:
[2. 2.1 2.2 2.3 2.4
2.5 2.6 2.7 2.8 2.9]
Generate a random integer from 0 to 100
PROGRAM:
from numpy import random
x = random.randint(100)
print(x)
OUTPUT:
52
Generate a random float from 0 to 1
PROGRAM:
from numpy import random
x = random.rand()
print(x)
OUTPUT:
0.9933233154569852
Generate a 1-D array containing 5 random integers from 0 to 100
PROGRAM:
from numpy import random
x=random.randint(100, size=(5))
print(x)
OUTPUT:
[3 32 43 14 52]
Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
PROGRAM:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)
OUTPUT:
[[90 99 11 30 34]
[66 40 63 36 37]
[63 35 89 51 58]]
Generate a 1-D array containing 5 random floats
PROGRAM:
from numpy import random
x = random.rand(5)
print(x)
OUTPUT:
[0.4439275
0.9761481 0.1597992
0.7203037
0.9134485]




