import numpy as np
import numpy.linalg as la

with open("A.txt",'r') as f:
    lines=f.readlines()
    A = np . array ([[ float( num ) for num in line . split () ] for line in lines ])

with open("x.txt",'r') as f:
    lines=f.readlines()
    x = np . array ([[ float( num ) for num in line . split () ] for line in lines ])


def powmet(A,x,M):
    for k in range(M):
        x=x/la.norm(x)
        x1= A@x #np.matmul(A,x)= A@x
        p=np.vdot(x1,A@x1)/(np.vdot(x1,x1))
        x=x1
        print("iteration number : " , k , '\n' , p)   

print(powmet(A,x,10))
print(np.max(la.eigvals(A)))

