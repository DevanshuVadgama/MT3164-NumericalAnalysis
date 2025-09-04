def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

t=int(input("Enter number of integers : "))
l={}
for i in range(t):
    x=int(input("Enter number : "))
    l[x]=fibo(x)
print(l) 