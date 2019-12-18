import time
from math import gcd, floor, sqrt
import re


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
                a.append(a[i - 1] + a[i - 2])
            i += 1
    return a[len(a) - 1] + a[len(a) - 2]


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
    arr.sort(key=lambda x: x[0] / x[1])
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


def check_brackets_seq(s):
    a = []
    for char in s:
        if char in {'(', '['}:
            a.append(char)
        else:
            if len(a) == 0:
                return False
            top = a.pop()
            if top == '(' and char != ')' or top == '[' and char != ']':
                return False
    return len(a) == 0


def check_bracket_cond(s):
    stack = []
    num = []
    answer = 0
    i = 0
    for char in s:
        if char in {'(', '[', '{'}:
            stack.append(char)
            num.append(i)
        elif char in {')', ']', '}'}:
            if len(stack) == 0:
                answer = i + 1
                break
            else:
                top = stack.pop()
                if top == '(' and char == ')' or top == '[' and char == ']' or top == '{' and char == '}':
                    num_top = num.pop()
                else:
                    answer = i
        i += 1
    if len(stack) == 0 and answer == 0:
        return 'Success'
    else:
        return answer


def get_tree_height(a):
    forest = []
    q = 0
    for i in a:
        if i in forest:
            forest.index(i)
        else:
            forest.append(i)
        q += 1


def dfs(n):
    matrix_of_coherence = [[0, 1, 0],  # матрица связности
                           [1, 0, 0],
                           [0, 0, 0]]

    ex = set()  # множество посещенных вершин

    def dfs1(node):  # start - начальная вершина
        ex.add(node)
        for coherence in range(len(matrix_of_coherence)):
            if matrix_of_coherence[node][coherence] == 1 and coherence not in ex:
                print(coherence)
                #  start(coherence)


def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_graph in graph[start] - visited:
        dfs2(graph, next_graph, visited)
    return visited


def reg_exp1(s):
    #  result = re.search('\d{2}-\d\d/\d{4}', s)
    result = re.search(r'\d{3}', s)
    ans = re.match(r'[-+]?\d+', '1234')
    print(ans[0] if ans else 'not found')
    print(result[0] if result else 'not found')


def reg_exp_exec():
    match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
    print(match[0] if match else 'Not found')
    # -> 23-12
    match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
    print(match[0] if match else 'Not found')
    # -> Not found
    match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
    print('YES' if match else 'NO')
    # -> YES
    match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
    print('YES' if match else 'NO')
    # -> NO
    print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'))
    # -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']
    print(re.findall(r'\d\d\.\d\d\.\d{4}',
                     r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
    # -> ['19.01.2018', '01.09.2017']
    for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
        print('Дата', m[0], 'начинается с позиции', m.start())
        # -> Дата 19.01.2018 начинается с позиции 20
    # -> Дата 01.09.2017 начинается с позиции 45
    print(re.sub(r'\d\d\.\d\d\.\d{4}',
                 r'DD.MM.YYYY',
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))


def reg_exp():
    reg_exp1('asdawadsad23-34/2020 not -a123a sfdsfd')
    reg_exp_exec()


def bin_search(input_l, val):
    list_size = len(input_l) - 1

    idx0 = 0
    idxn = list_size
    # Find the middle most value
    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if input_l[midval] == val:
            return midval
    # Compare the value the middle most value
        if val > input_l[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1
    if idx0 > idxn:
        return None


if __name__ == '__main__':
    #  compare_fib_methods(40)
    #  print(get_fib_last_digit(696352))
    #  print(get_fib_n_mod_m(10, 2))
    #  compare_gcd(124000, 800000)
    #  greedy_algor([[1, 3], [2, 5], [3, 6]])
    #  greedy_algor([[4, 7], [1, 3], [2, 5], [5, 6]])
    #  expensive_bug([3, 80], [[60, 20], [100, 50], [120, 30]])
    #  get_s(6)
    #  print(check_brackets_seq("()[[()]]"))
    #  print(check_bracket_cond("()[]}"))
    #  print(check_bracket_cond('(slkj{lk[lsj]}'))
    #  print(get_tree_height([9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))
    graphIn = {'0': set(['1', '2']),
               '1': set(['0', '3', '4']),
               '2': set(['0']),
               '3': set(['1']),
               '4': set(['2', '3'])
               }
    #  print(dfs2(graphIn, '0'))
    #  reg_exp()
    input_l = [20, 70, 109, 304, 530, 702]
    print(bin_search(input_l, 530))
    print(bin_search(input_l, 110))

