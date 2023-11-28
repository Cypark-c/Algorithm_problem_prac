'''
[아이디어]
1. first: pop
    1-2. else: first pop and append
'''
import sys
from collections import deque

input=sys.stdin.readline
N=int(input())

queue=deque([i for i in range(1,N+1)])
# 문제의 절차 수행
for _ in range(N-1):
    print(queue.popleft(),end=' ')
    queue.append(queue.popleft())
print(queue.popleft())