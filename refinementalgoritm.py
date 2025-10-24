import numpy as np
import numpy.linalg as la


with open("A.txt",'r') as f:
    lines=f.readlines()
    A = np . array ([[ float( num ) for num in line . split () ] for line in lines ])

with open("x0.txt",'r') as f:
    lines=f.readlines()
    x0 = np . array ([[ float( num ) for num in line . split () ] for line in lines ])

with open("b.txt",'r') as f:
    lines=f.readlines()
    b = np . array ([[ float( num ) for num in line . split () ] for line in lines ])

def iterrefi(k,x0,b,A):
    # k iterations
    for i in range(k):
        x1=x0
        r=b-np.matmul(A,x1)
        if la.norm(r)<10**-5:
            return "Final soln after " ,i+1 , " iterations : " ,   x1 
        else:
            e=la.solve(A,r)
            x1=x1+e
    return x1        

x=iterrefi(10,x0,b,A)  
print(la.norm(np.matmul(A,x)-b))