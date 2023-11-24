'''
[아이디어]: 단순한  큐
'''
from collections import deque
import sys

queue=deque()
input=sys.stdin.readline
N=int(input())
for _ in range(N):
    cmd=input().rstrip()
    if 'push' in cmd:
        dummy,num=cmd.split()
        queue.append(int(num))
    elif cmd=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif cmd=='size':
        print(len(queue))
    elif cmd=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    else:
        pass
