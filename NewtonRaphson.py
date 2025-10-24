def f(x):
    return x**3 + 8*x**2 + x + 1

def df(x):
    return 3*x**2 + 16*x + 1

def raphsonmethod(x0, M, tol=1e-5):
    for k in range(M):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print(f"Iteration {k}: Zero derivative. No solution found.")
            return None
        x1 = x0 - fx / dfx
        print(f"Iteration {k}: x = {x0}, f(x) = {fx}, next x = {x1}")
        if abs(fx) < tol:
            print(f"Converged based on function value at iteration {k}.")
            return x0
        if abs(x1 - x0) < tol:
            print(f"Converged based on change in x at iteration {k}.")
            return x1
        x0 = x1
    print("Did not converge within the given iterations.")
    return x0

root = raphsonmethod(10, 100)
print("Root found:", root)
print("Function value at root:", f(root))
