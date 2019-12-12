import time
from builtins import print


def get_fib(n):
    if n <= 1:
        return 1
    else:
        return get_fib(n - 1) + get_fib(n - 2)


def get_fib_array(n):
    if n <= 1:
        return 1
    else:
        a = [0, 1]
        i = 1
        while i < n:
            if i != 1:
                a.append(a[i-1]+a[i-2])
            i += 1
    return a[len(a)-1] + a[len(a)-2]


def get_fib_variable(n):
    if n <= 1:
        return 1
    else:
        i = 1
        a1 = 0
        a2 = 1
        while i < n:
            a1, a2 = a2, a1 + a2
            i += 1
    return a2


def compare_fib_methods(n):
    #  _startTime1 = time.time()
    #  print(get_fib(n-1))
    #  print("Elapsed time: {:.3f} sec".format(time.time() - _startTime1))
    _startTime2 = time.time()
    print(get_fib_array(n))
    print("Elapsed time: {:.3f} sec".format(time.time() - _startTime2))
    _startTime3 = time.time()
    print(get_fib_variable(n))
    print("Elapsed time: {:.3f} sec".format(time.time() - _startTime3))


def get_fib_last_digit(n):
    if n <= 1:
        return 1
    else:
        i = 1
        a1 = 0
        a2 = 1
        while i < n:
            a1, a2 = a2 % 10, (a1 % 10 + a2 % 10) % 10
            i += 1
    return a2


def get_fib_n_mod_m(n, m):
    if n <= 1:
        return 1
    else:
        i = 1
        a1 = 0
        a2 = 1
        while i < n:
            a1, a2 = a2 % m, (a1 % m + a2 % m) % m
            i += 1
    return a2


def get_nod(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return get_nod(a % b, b)
    else:
        return get_nod(a, b % a)


if __name__ == '__main__':
    #  compare_fib_methods(40)
    #  print(get_fib_last_digit(696352))
    #  print(get_fib_n_mod_m(10, 2))
    print(get_nod(18, 12))


