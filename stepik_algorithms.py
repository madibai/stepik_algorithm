import time
from math import gcd, floor, sqrt


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


def get_gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return get_gcd(a % b, b)
    else:
        return get_gcd(a, b % a)


def get_gcd_another(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def get_gcd_2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def compare_gcd(a, b):
    startTime1 = time.time()
    print(get_gcd(a, b))
    print("Elapsed time: {:.3f} sec".format(time.time() - startTime1))
    startTime2 = time.time()
    print(gcd(a, b))
    print("Elapsed time: {:.3f} sec".format(time.time() - startTime2))
    startTime3 = time.time()
    print(get_gcd_another(a, b))
    print("Elapsed time: {:.3f} sec".format(time.time() - startTime3))
    startTime4 = time.time()
    print(get_gcd_2(a, b))
    print("Elapsed time: {:.3f} sec".format(time.time() - startTime4))


def greedy_algor(arr):
    arr.sort(key=lambda x: x[1])
    i = 0
    l = len(arr)
    sb = ""
    while i < l:
        point = arr[i][1]
        j = i
        while j < l and point <= arr[j][1] and point >= arr[j][0]:
            i = j
            j += 1
        sb += str(point) + " "
        i += 1
    print(len(sb[:-1].split(" ")))
    print(' '.join(str(s) for s in sb[:-1].split(" ")))


def expensive_bug(n, arr):
    arr.sort(key=lambda x: x[0]/x[1])
    arr = arr[::-1]
    q = n[0]
    w = n[1]
    j = []
    for i in arr:
        if q == 0 or w == 0:
            break
        elif i[1] >= w:
            j.append(i[0] / i[1] * w)
            w = 0
            q -= 1
        else:
            w = w - i[1]
            q -= 1
            j.append(i[0])
    print("{:.5f}".format(sum(j)))


def get_s(k):
    n = k * ((k + 1) / 2)
    print(n)
    x = floor((sqrt(1 + 8 * k) - 1) / 2) - 1
    print(x)


if __name__ == '__main__':
    #  compare_fib_methods(40)
    #  print(get_fib_last_digit(696352))
    #  print(get_fib_n_mod_m(10, 2))
    #  compare_gcd(124000, 800000)
    #  greedy_algor([[1, 3], [2, 5], [3, 6]])
    #  greedy_algor([[4, 7], [1, 3], [2, 5], [5, 6]])
    #  expensive_bug([3, 80], [[60, 20], [100, 50], [120, 30]])
    get_s(6)

