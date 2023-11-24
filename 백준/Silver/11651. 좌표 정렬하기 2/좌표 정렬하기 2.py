import sys
input=sys.stdin.readline
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda k: (k[1],k[0]))
for item in A:
    print(*item)