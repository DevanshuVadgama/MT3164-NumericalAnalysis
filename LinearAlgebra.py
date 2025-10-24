import math
import numpy as np
import numpy.linalg as la

with open("MatrixA.txt",'r') as f:
    lines=f.readlines()
    A = np . array ([[ float( num ) for num in line . split () ] for line in lines ])
    
with open("MatrixB.txt",'r') as f:
    lines=f.readlines()
    B= np . array ([[ float( num ) for num in line . split () ] for line in lines ])
    
print(  " Matrix A : \n " , A)
print ( " Matrix B : \n " , B)

print(np.matmul(A,B))
print(A+B)
print(la.norm(A,ord=2))
print("Frobneius norm : " , '\n' , la.norm(A))
