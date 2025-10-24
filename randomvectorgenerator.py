import random
import numpy as np

def vec(n):
    v=np.random.uniform(1,10,size=n)
    return v

v=vec(10)
np.savetxt("x0.txt", v , fmt="%.3f")
