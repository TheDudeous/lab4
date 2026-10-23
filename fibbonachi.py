def fib():
    a_0 = 0
    a_1 = 1
    while True:
        yield a_1
        a_0, a_1 = a_1, a_0 + a_1

f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

