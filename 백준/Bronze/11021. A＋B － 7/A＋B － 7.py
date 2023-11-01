import sys
N=int(input())
for i in range(1,N+1):
    print(f"Case #{i}:",sum(map(int,sys.stdin.readline().split())))