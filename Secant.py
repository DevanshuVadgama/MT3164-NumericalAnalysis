def f(x):
    return x**3+8*x**2+x+1

def secant_method(x0,x1,M):
    for i in range(M):
        a=f(x0)
        b=f(x1)
        if abs(a-b)<10**-5 or abs(x1-x0)<10**-5:
            return (x1+x0)/2
        else:
            x2=x1-b*((x1-x0)/(b-a))
            x0=x1
            x1=x2
    return (x0+x1)/2

x=secant_method(-7,8,100)
print(x)
print(int(f(x)))