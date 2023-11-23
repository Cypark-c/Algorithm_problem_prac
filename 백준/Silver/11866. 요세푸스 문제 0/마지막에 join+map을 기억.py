import sys

input = sys.stdin.readline

n,k = map(int,input().split())
que = []
for i in range(1,n+1):
    que.append(i)
li = []
idx = 0

while que:
    idx += k-1
    if idx >= len(que):
        idx %= len(que)
    li.append(str(que.pop(idx)))

print("<{}>".format(', '.join(map(str, li))))
