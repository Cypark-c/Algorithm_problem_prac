'''
BFS라 생각했는데 그게 아니었음!
[아이디어]
[조건]
- 좌표로 진행함(0,0)이 가장 위쪽 (r+1),(c+1)
- 청소되지 않았다면 현재 칸을 청소
    [case: 주변 4칸 그 무엇도 청소되지 않은 빈 칸이 없다면]
    - ☆청소 후 빈 칸이 없다면 일단 후진을 시도, 가능하면 후진
    - ☆만약에 후진이 불가능함(벽) 이면 작동 Stop

    [case: 주변 4칸 중 청소해야 하는 빈칸이 있다면]
    - ☆반시계 rotate 한다. 언제까지? 청소되지 않은 빈칸을 찾을 때까지
    - 그 후 그 칸으로 전진

[함수 구성]
- 주의해야할 부분은 벽은 후진을 못하는데 청소한 구역이라 해도 후진만큼은 가능!
- 또한 BFS의 주의점은 방문을 하는 경우에 큐에 넣기 전에 방문처리 하는게 좋기는함
- 청소한 영역의 개수를 구함. 그런데 이게 약간 불명확한듯
- 일단은 영역 복제해야할수도. 아님 그냥 쭉 진행하면서 카운팅 늘리거나

그런데 처음에 BFS라고 생각했는데 다시 보니까 시뮬레이션 인듯함
'''

# BFS 함수, 초기 좌표는 넣어주도록 한다.
def BFS(r,c,d):
    # 초기에 청소기가 있는 자리는 방문처리 무조건 해야함
    # 내 경우는 한번 방문한 영역은 -1로 처리하기로함
    graph[r][c]=-1
    queue=deque([(r,c)]) # 초기 좌표 대입으로 생성
    count=1 # 청소한 영역의 갯수

    # 큐가 비어있지 않은 동안에 진행
    while queue:
        r,c=queue.popleft()

        '''
        어차피 맵상에서 0이나 -1만 따라 이동할 거니까 -1이 아니면 청소 안했음
        그 때만 카운트를 늘리면 됨
        '''
        if graph[r][c]==0:
            count+=1
            graph[r][c]=-1

        # 어떻게 방향을 진행할까는 현재 방향에 의해 결정된다.
        # d에 관한 방향을 설정하기 (반시계로 90도씩 회전함)
        flag=0
        orig_d=d
        for _ in range(4):

            # 반시계 회전을 구현
            if 0<d<4:
                d=d-1
            else:
                d=3

            # 빈칸에 대한 처리를 하기
            # 방향을 탐색하면서 청소하지 않은 빈칸이 나오면 break하고 큐에 넣어야함
            nr=r+dir_r[d]
            nc=c+dir_c[d]

            if (-1<nr<N and -1<nc<M) and (graph[nr][nc]==0):
                queue.append((nr,nc))
                flag=1
                break
        # 방향 4개 그 어떠한 것도 찾지 못했을 경우 (4칸 모두 칠해지거나 벽)
        if flag==0:
            d=orig_d # for문 지나기 전 원래의 방향
            nr=r-dir_r[d]
            nc=c-dir_c[d]
            if (-1 < nr < N and -1 < nc < M) and (graph[nr][nc]!=1):
                queue.append((nr,nc))
            else:
                break

    return count

import sys
from collections import deque

input=sys.stdin.readline

# 첫째 줄에 입력되는 바으이 크기
N,M=map(int,input().split())

# 로봇 청소기가 있는 칸의 좌표와 방향
# 초기 청소기 방향: 0,1,2,3 # 북,동,남,서 (문제에서 이렇게 하라고 함)
# 방향벡터도 북,동,남,서로 정하자.
dir_r=[-1,0,1,0]
dir_c=[0,1,0,-1]

r,c,d=map(int,input().split()) # r,c 는 초기 좌표, d는 초기 방향

# map 입력
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))

print(BFS(r,c,d))