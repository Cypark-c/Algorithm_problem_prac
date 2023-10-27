import sys
T=int(input())
for _ in range(T):
    X=list(map(str,sys.stdin.readline().rstrip()))
    print(X[0]+X[-1])