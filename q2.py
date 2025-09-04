def f(x):
    return x**3-5*x**2+3*x-7
def df(x):
    return 3*x**2-10*x+3   

def NewtonRaph(M,x0):
    for i in range(M):
        fx=f(x0)
        dfx=df(x0)
        print("iteration number :",i)
        x1=x0-(fx/dfx)
        if abs(x1-x0)<0.0001 or abs(f(x1))<0.0001:
            return x1
        else:
            x0=x1
            print("expected root is : ",x1)
    return x0
x0=float(input("Enter initial guess : "))
M=int(input("Enter maximum iterations : "))
root=NewtonRaph(M,x0)
print("Root is : ",root)