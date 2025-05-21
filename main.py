def fib():
    a = 0
    b = 1
    n = 100000
    c = 0
    while c < n:
        c = a + b
        b = a
        a = c
        print(c)

fib()
