import numpy as np
import random

def gen(m, n):
    arr = np.random.randint(1, 10, size=(m, n))
    return arr

arr = gen(7,19)
np.savetxt("A.txt", arr, fmt="%.3f")
