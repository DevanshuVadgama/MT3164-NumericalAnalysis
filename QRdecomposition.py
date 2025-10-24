import numpy as np
import numpy.linalg as la

with open("A.txt",'r') as f:
    lines=f.readlines()
    A=np.array([[float(num) for num in line.split()] for line in lines])

with open("b.txt",'r') as f:
    lines=f.readlines()
    b=np.array([[float(num) for num in line.split()] for line in lines])

with open("x0.txt",'r') as f:
    lines=f.readlines()
    x0=np.array([[float(num) for num in line.split()] for line in lines])

def qrdecomposer(A):
    return la.qr(A)

arr=qrdecomposer(A)
Q=arr[0]
R=arr[1]
QT=Q.T

# tried gradient descent but it is too slow!!
# def sol(A, x0, b, M):
#     b_eff = QT @ b
#     x = x0
#     for i in range(M):
#         v = b_eff - R @ x
#         t = float((v.T @ v) / (v.T @ (R @ v)))  
#         x = x + t * v
#     return x

# z=sol(A,x0,b,100) 
# y=la.solve(R,Q.T@b)       
# print(la.norm(z-y))

x=la.lstsq(R,Q.T@b)[0]
print("least square soln : " , x) #using qr decomposer

print("trace of Q = ", np.trace(Q),np.size(Q))
print("trace of R = ",np.trace(R),np.size(R))

