def f(x):
    return (x**3+4*x**2+3*x+5)/(2*x**3-9*x**2+18*x-2)

def bisection_method(f,a,b,M,d,e):
    if f(a)*f(b) >= 0 or a >= b:
        print("Bisection method fails.")
        return None
    for i in range(M):
        c = (a + b) / 2
        if abs(f(c)) < e or (b - a) / 2 < d:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

bisection_root = bisection_method(f,-5,0, 100, 1e-5, 1e-5)
print("Root found by Bisection Method:", bisection_root)