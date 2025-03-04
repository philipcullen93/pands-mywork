def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

ans = fibonacci(10)
print(f"Fibonacci sequence is {ans}")