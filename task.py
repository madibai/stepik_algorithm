import sys
from collections import deque


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


if __name__ == '__main__':
    #  print(task1_1(input()))
    task1_2()
