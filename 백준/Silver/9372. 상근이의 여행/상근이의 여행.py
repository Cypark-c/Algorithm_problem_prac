#[아이디어]
'''
일단 비행기 표를 통해서 맵을 생성할 수 있음.
그래프 맵이 하나 만들어지면, 그 맵을 통해서 이동이 가능할 듯
[[], [2, 3], [1, 3], [1, 2]]면
1->2->3 이게 맞긴 한데
1->2->1->3 이런 것도 가능은 하다는 뜻.

그렇기는 한데, 최소로 이동을 하고 싶어함. 일단은 방문지를 콜렉팅할 리스트를 선언하고
그 리스트가 꽉차면 종료하는 식으로 프로그램을 짜보기

양방향 그래프.. 아직 안배운 부분이긴 한데
기억해 두었다가 복습이 필요. 그리고 애초에 이 문제는 무조건 노드-1이 답이다..
'''

def DFS_BK(v,cnt):
    visited[v] = 1

    for item in graph[v]:
        if visited[item]==0:
            cnt=DFS_BK(item,cnt+1)
    return cnt

import sys
input=sys.stdin.readline
T=int(input()) # 테스트 케이스 수
for _ in range(T):
    N,M=map(int,input().split()) # 국가의 수, 비행기의 종류
    graph=[[] for _ in range(N+1)] # 국가의 수 +1 만큼 그래프를 생성
    # graph mapping
    for _ in range(M):
        start,end=map(int,input().split())
        graph[start].append(end)
        graph[end].append(start)

    # 이건 양방향 그래프이므로 어차피 따라가다보면 모든 노드를 순회하게 되어있음
    visited = [0]*(N+1)

    print(DFS_BK(1, 0))