# 매우 기초적인 BFS
from collections import deque
import sys
input=sys.stdin.readline
N,M,R=map(int,input().split())

LOCs=[0 for i in range(0,N+1)] # 정점, 0이란 정점은 사용하지 않음, 모두 0으로 초기화
Graph=[[] for _ in range(N+1)] # 노드에서 간선 관계를 표현

for _ in range(M):
    start,end=map(int,input().split())
    Graph[start].append(end)
    Graph[end].append(start)
for i in range(1,N+1):
    Graph[i].sort()

#print(Graph)

def BFS(LOCs,Graph,start):
    queue=deque([start])
    order=0
    order+=1
    LOCs[start]=order

    # 큐의 자료구조 특성을 꼭 생각해야함
    while queue:
        v=queue.popleft()
        for node in Graph[v]:
            if LOCs[node]==0:
                queue.append(node)
                order+=1
                LOCs[node]=order

BFS(LOCs,Graph,R)
for i in range(1,N+1):
    print(LOCs[i])