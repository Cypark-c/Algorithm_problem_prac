# 람다식 잘 알고있나
import sys
N=int(input())
input=sys.stdin.readline
pos=[]
for _ in range(N):
    x,y=map(int,input().split())
    pos.append([x,y])
pos.sort(key=lambda k: (k[0],k[1]))
for item in pos:
    print(item[0],item[1])