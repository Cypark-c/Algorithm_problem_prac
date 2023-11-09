from collections import deque # for BFS

N,M,V=map(int,input().split()) # N: 정점, M: 간선, V:탐색 시작 정점
# 처음에 간선 정보들을 받음 간선이라는 것은 두 지점을 연결하는 것
graph=[[] for _ in range(N+1)] # 0번 점은 미사용 할 것
for _ in range(M):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
for item in graph:
    item.sort() # sort
# print(graph) #← 실행시켜보면 그래프 초기화 된 것을 확인 가능함

Visit_list=[0 for _ in range(N+1)] # 마찬가지로 0번 점은 미사용 한다. 방문하지 않았으면 0
# DFS는 재귀적 호출이 필요함
# 어떻게 구성할지 생각해보니
def dfs(Graph,Visited,V): # 함수 수정 필요함
    if Visited[V]==1:
        return

    if Visited[V]==0:
        Visited[V]=1 # 방문을 표시
        print(V,end=' ')
        for place in Graph[V]:
            dfs(Graph,Visited,place)

# DFS 완성
dfs(graph,Visit_list,V)



print("")
# Visit 초기화 필요한가? Yes
#print(Visit_list)
for i in range(N+1):
    Visit_list[i]=0


def bfs(Graph,start,visited):
    # 큐를 선언
    queue=deque([start])
    visited[start]=1 # 방문처리
    while queue: #큐가 빌 때까지 반복해야한다.
        v=queue.popleft() # 큐에서 하나를 뽑음
        print(v,end=' ') # 방문한 노드를 출력

        for i in graph[v]:
            if not visited[i]: # v노드와 이웃한 i라는 노드에 방문하지 않았다면
                queue.append(i) # 해당 노드를 큐에 추가
                visited[i]=1 # 방문처리


bfs(graph,V,Visit_list)

