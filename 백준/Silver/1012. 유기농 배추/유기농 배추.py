'''
[아이디어]
흰지렁이는 인접한 배추로 이동이 가능하다. 그냥 군집 찾아서 카운트하면됨
그리고 BFS로 풀면 될것 같음. 어디선가 DFS랑 BFS가 각각 좋은 상황 나쁜 상황이 있다고 들은듯 하다.
이 문제가 끝나면 확인해봐야 할 일
1. Map 정보 확인
2. 배추가 있는 곳은 1로 지정
3. 탐색하다가 행렬 벗어나거나 사방이 전부 벽으로 막혔거나 방문 힘들면 return
    - 탐색할때는 동서남북을 살펴보는게 좋겠다. 방향벡터를 도입한다
4. 2~3과정이 완료될 때 마다 군집이 증가


[변수]
-군집을 cluster라고 하자
'''

import sys
input=sys.stdin.readline
T=int(input()) # 테스트 케이스 수

# BFS 함수
from collections import deque # BFS를 활용하기 위한 큐의 선언

# 동서남북 방향벡터
dc=[1,-1,0,0]
dr=[0,0,1,-1]

def BFS(graph,r,c):

    queue=deque()
    queue.append([r,c])
    # graph[r][c]=-1 # 방문한 위치는 -1로 처리함

    while(queue):
        r,c=queue.popleft()

        for i in range(4): # 방향 탐색을 위한 for 문
            nc=c+dc[i]
            nr=r+dr[i]
            if (-1<nc<M and -1<nr<N) and not (graph[nr][nc]==0):
                queue.append([nr,nc])
                graph[nr][nc] = 0
    return


for _ in range(T):
    bugs=[]
    M,N,K=map(int,input().split()) # 지도 크기
    Box=[[0]*M for _ in range(N)] # 지도 초기화
    cluster=0 # 군집
    for _ in range(K):
        i,j=map(int,input().split()) # 배추 위치 정보 전송
        Box[j][i]=1 # 하필 문제에서 가로 세로 바꿔서 받았음
        bugs.append([j,i]) # bug라는 행렬에 위치정보 1을 저장함

    # BFS 탐색
    for item in bugs:
        if Box[item[0]][item[1]]==1:
            BFS(Box,item[0],item[1])
            cluster+=1
    print(cluster)