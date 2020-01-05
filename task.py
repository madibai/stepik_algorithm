import sys
from collections import deque

from urllib3.connectionpool import xrange


def task_tree_depth():
    n = int(input())
    s = list(map(int, input().split()))
    n = len(s)
    d = {}

    def up(v):
        next_v = s[v]
        if next_v == -1:
            return 1
        if v not in d:
            d[v] = up(next_v) + 1
        return d[v]

    mx = 0
    for i in range(n):
        mx = max(mx, up(i))
    print(mx)


def task1_1(string):
    braces = {')': '(', '}': '{', ']': '['}
    stack = []
    for i, c in enumerate(string, start=1):
        if c in braces.values():
            stack.append((c, i))
        if c in braces and (not stack or braces[c] != stack.pop()[0]):
            return i
    return stack.pop()[1] if stack else 'Success'


def task1_2():
    reader = (map(int, s.split()) for s in sys.stdin)
    size, n = next(reader)
    times = deque()
    for a, d in reader:
        while times and times[0] <= a:
            times.popleft()
        if len(times) < size:
            if times:
                a = max(a, times[-1])
            print(a)
            times.append(a + d)
        else:
            print(-1)


class StackWithMax:
    def __init__(self):
        self._stack = []

    def push(self, n):
        if not self._stack:
            self._stack.append([n, n])
        else:
            self._stack.append([n, max(self._stack[-1][1], n)])

    def pop(self):
        return self._stack.pop()[0]

    def max(self):
        return self._stack[-1][1]


def task1_3():
    stack = StackWithMax()
    n_ = int(input())

    for line in sys.stdin.readlines():
        #  n_ -= 1
        if line.startswith('pop'):
            stack.pop()
        elif line.startswith('max'):
            print(stack.max())
        else:
            command_, value = line.split()
            stack.push(int(value))
        print(n_)


def task3_1():
    n_ = int(input())
    a = {}
    for i in xrange(n_):
        line = input()
        if line.startswith('add'):
            a[line.split(' ')[1]] = line.split(' ')[2]
        elif line.startswith('find'):
            if line.split(' ')[1] in a:
                print(a[line.split(' ')[1]])
            else:
                print('not found')
        elif line.startswith('del'):
            if line.split(' ')[1] in a:
                a.pop(line.split(' ')[1])


if __name__ == '__main__':
    #  task_tree_depth()
    #  print(task1_1(input()))
    #  task1_2()
    #  task1_3()
    task3_1()

