'''
[아이디어]
사람들은 번호로 표시됨
1. 부모와 자식은 1촌
2. 나와 할아버지는 2촌
3. 아버지의 형제와 나는 3촌
(나-아버지-할아버지-아버지형제) 이런식으로 3촌

두 노드가 결국 몇 촌인지를 가늠해보면 된다.

재귀함수는 항상 리턴을 주의해야함.
'''

# 탐색함수
def DFS(v,edge,target): # v는 방문 노드, edge는 촌수를 나타냄
    global result
    visited[v]=1 # 방문체크

    # 종료조건1. target을 찾았을때.
    if v==target:
        result=edge
        return

    # 종료조건2.
    # 종료조건은 현재 노드에서 더 방문을 못한다면 멈추는 것으로 하면 될 것 같음
    flag=0
    for next in graph[v]:
        if visited[next]==1: # 방문을 했다면
            flag+=1
    if flag==len(graph[v]): # 현재 노드에서 이웃한 노드들의 갯수와 flag가 동일하면
        return

    # 방문하지 않은 노드들 방문
    for next in graph[v]:
        # 방문하지 않은 노드에 대해서 방문하기
        if visited[next]!=1:
            DFS(next,edge+1,target)

import sys
input=sys.stdin.readline

# 전체 사람의 수
n=int(input())
# 촌수를 계산해야하는 서로 다른 두 사람의 번호 (노드)
a,b=map(int,input().split())

# 부모와 자식들간 관계의 개수
m=int(input())

# 방문여부 확인노드
visited=[0 for _ in range(n+1)]
visited[0]=1 # 사용하지 않는 노드인데 그냥 방문처리 해줌

# 그래프
graph=[[] for _ in range(n+1)] # 0번째 노드는 사용하지 않을 것
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)
result=-1
DFS(a,0,b)
print(result)