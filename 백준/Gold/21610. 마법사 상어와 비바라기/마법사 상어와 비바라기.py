'''
[아이디어]

맞은 것 같은데 시험볼 때 실수 안하게 조심하자 더하기를 중복한다든지 하는거

빡구현 문제인듯
방향:
    ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    1, 2, 3 ,4 ,5, 6, 7, 8

구름생성 및 이동
    - 생성경계
        - 대각선으로 1의 거리이나
        처음의 경계를 넘어간 경우라면 대각선 경계로 인정하지 않음
    - 그냥 물생성
        - 구름이 비 내려서 구름이 있던 위치에 물이 1증가
        - 일단 이 단계에서 구름은 한번 사라짐

    - 물복사버그로 물 생성
        - 각 칸에 대해서 대각선 거리가 1인 곳에 바구니가 몇 개가 있느냐
        이것이 A[r][c]의 물 증가 정도를 결정함

    - 물 생성 과정을 A[r][c]에 대해 일반 물생성과 물복사 버그를 마친 다음
    모든 맵에 대해 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름 생성 그 후
    구름을 생성한 칸은 물의 양을 2 줄임
        - ★이 때 구름이 사라진 칸에서는 구름이 생길 수 없다

    - d,s는 문제에서 말한 방향과 구름이 얼마나 이동하는가를 나타냄
문제에서 말한 1번행=그래프 0번행 이런식으로 이해하자. 그게 편할듯



'''
# ★ 모든 구름이 d 방향으로 s칸 이동한다.
#    ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# d= 1, 2, 3, 4, 5, 6, 7, 8
# 위치를 받아서 구름을 이동시키는 함수!
# 구름이 있는 위치를 clouds라는 큐에 넣어버리고 시작하기
def move(d,s,clouds):
    visited=[[0]*N for _ in range(N)] # visited 배열 생성
    dir=[[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
    i,j=dir[d-1] # d에 따라 결정되는 무브먼트

    # clouds 란 놈들의 이동 어떻게 구현할까
    # 내 생각엔 구름을 이동 시킨다음에 방문처리를 해서
    # 여기는 차후 구름생성 안된다라고 표시하는게 좋을 듯

    while clouds:
        p,q=clouds.popleft() # 구름이 들어있는 위치에서 하나 꺼내기
        # s만큼 방향벡터로 이동을 하면서 각 구름별 최종 위치를 만들기
        for _ in range(s): # s만큼 구름을 이동시켜보기
            # 행에 대한 다음위치 처리하기
            if p+i<0:
                p=N-1
            elif 0<p+i<N:
                p=p+i
            else: # p+i>=N 인 케이스
                p=0

            # 열에 대한 다음위치 처리하기
            if q+j<0:
                q=N-1
            elif 0<q+j<N:
                q=q+j
            else: # q+j>=N 인 케이스
                q=0

        visited[p][q]=1 # 방문처리

    return visited # 구름들의 최종 위치를 반환함. 이제 이 위치는 물생성이 불가능!

# 구름을 만드는 함수
def make_clouds(visited):

    water_copy=deque() # 물복사 버그를 위해 큐를 미리 선언

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가함
    for row, line in enumerate(graph):
        for col,value in enumerate(line):
            if visited[row][col]==1: # 구름이 있다면
                graph[row][col]+=1 # 그래프의 물의 양 증가
                water_copy.append((row,col)) # 현재 구름 위치를 큐에 넣음
    # 구름이 모두 사라진다. (일단 구름이 있는 위치 자체는 킵하자)

    # 물복사버그
    diagonal=[[-1,-1],[-1,1],[1,-1],[1,1]] # 물복사 버그 위한 대각선
    while water_copy:
        r,c=water_copy.popleft()
        sum=0

        # 대각선 중 접근 가능한 칸에 대해서 물을 모은다
        for k in range(4):
            nr=r+diagonal[k][0]
            nc=c+diagonal[k][1]
            if 0<=nr<N and 0<=nc<N and graph[nr][nc]!=0:
                sum+=1
        # print((r,c),sum)
        graph[r][c]+=sum

    # 바구니에 저장된 물의 양이 2인 이상인 모든 칸에 구름만들고 물의 양 줄이기
    # 원래 구름이 있던 곳은 물을 생성하지 말 것.
    clouds_new=deque()
    for row, line in enumerate(graph):
        for col,value in enumerate(line):
            # 구름이 없다면 혹은 생성되지 않았다면
            if graph[row][col]>=2 and visited[row][col]==0:
                graph[row][col]-=2 # 물의 양을 2 줄이고
                clouds_new.append((row,col)) # 새로운 구름 생성 큐에 추가

    # print(clouds_new)
    return clouds_new # 새롭게 구름 생성한 큐를 돌려준다!

from collections import deque
import sys

input=sys.stdin.readline
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dir=[1,2,3,4,5,6,7,8] # 방향을 결정

# 구름의 초기 위치 비바라기 기술의 시작
clouds=deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

'''
for line in graph:
    print(line)
print("\n")
'''

for _ in range(M):
    d,s=map(int,input().split())
    clouds=make_clouds(move(d, s, clouds)) # visited가 리턴됨. 그걸 make_clouds에 넣음
    '''
    for line in graph:
        print(line)
    print("\n")
    '''

result=0
for row, line in enumerate(graph):
    for col,value in enumerate(line):
        result+=graph[row][col]

print(result)