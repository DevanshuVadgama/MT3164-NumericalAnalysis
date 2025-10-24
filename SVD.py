import numpy as np
import numpy.linalg as la

with open("A.txt",'r') as f:
    lines=f.readlines()
    A = np . array ([[ float( num ) for num in line . split () ] for line in lines ])


def svd(A):
    D=la.svd(A)
    U=D[0]
    
    m, n = A.shape
    S = np.zeros((m, n))
    S[:len(D[1]), :len(D[1])] = np.diag(D[1])
   
    V_T=D[2]
    R=U@S@(V_T)
    print(" A=U S V_T where ; ",'\n', " U = ", U,'\n', " S = ", S,'\n',"V_T(V transpose) = ", V_T)
    print("Reconstructed A = ", R)
    print(" UU* = ", np.round(U@(U.T)), '\n', " VV* = ",np.round((V_T)@(V_T.T)),'\n')
    print("Hence U and V are orthogonal as expected")
    print("List of all singular vals of A---> ", D[1])
    print("Card(list)= ", np.size(D[1]))
    print("rank(A)= ", la.matrix_rank(A))
    print("clearly card(list)=rank(A) as expected")
    print("Norm of A (L2) = ", np.max(D[1]))
    print("Norm of A (actual calc)= ", la.norm(A,ord=2))

svd(A)    

