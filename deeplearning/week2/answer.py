import numpy as np
import random
a = np.array([1,2,3])
b = np.array([3,4,5])
c = np.outer(a,b)
print c
print '*'*10 + 'element-wise multiply' + '*'*10
d = np.multiply(a,b)
e = a * b
print d
print e
