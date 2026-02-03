def is_fib(x):
    b = 5 * (x ** 2) + 4
    c = 5 * (x ** 2) - 4
    if int(b**0.5)*int(b**0.5)==b or int(c**0.5)*int(c**0.5)==c:
        return True
    return False

a = int(input())
c = 1

if is_fib(a):
    for i in range(1, a+1):
        if is_fib(i):
            c += 1
    print(c)
else:
    print(-1)






