'''
[아이디어]
- 전형적인 DFS,BFS 문제.
    양방향 그래프이니 그래프 관계를 초기화 하면 풀 수 있다.
- visited를 사용하여 방문여부를 체크해 가면서 탐색하도록 한다
'''
def DFS(node,visited):
    visited[node]=1 # 방문처리
    for new in graph[node]:
        if visited[new]==0: # 아직 방문하지 않았다면
            DFS(new,visited)
    return

import sys
input=sys.stdin.readline
N=int(input()) # 컴퓨터 수
M=int(input()) # 직접 연결되어 있는 쌍의 수

visited=[0 for _ in range(N+1)] # 0번노드는 사용하지 않음
graph=[[] for _ in range(N+1)] # 그래프 초기화

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1,visited)
print(visited.count(1)-1) # 첫번째 노드인 1은 1번 노드 자체가 감염된거지 1번을 통해서 감염된 건 아니니까