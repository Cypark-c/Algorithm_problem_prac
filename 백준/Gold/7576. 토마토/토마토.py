'''
★좋은 문제니 반복 복습해야함!
[아이디어]
익지 않은 토마토가 익은 토마토의 영향을  받고, 동서남북으로 영향을 받음
미로탐색이랑 비슷하면서도 다른게 토마토가 며칠이 지나면 전부 익는가가 핵심
BFS 기법으로 풀어본다.

- N(세로,행),M(가로,열)
- 내 생각엔, BFS로 하나를 방문할 때 마다 카운트 수를 증가시킴. 그 카운트를 세서 맥시멈 값을 추출하면 될 듯함
    - -1이 들어있는 칸은 진행하지 못함을 기억!
        → 그렇다면 방문한 곳을 -1로 표시하면 된다.
        → 보통 visited 배열을 따로 만들어서 생각을 하기도 하던데 안되면 저렇게 가고 일단 내 방식대로 풀어보기
    - 익은 토마토가 여러 개 들어 있을 수 있음
    - 그런 경우 출발 지점을 여러개를 두어야 한다.
    - 이 말은 처음에 1을 전부 찾아서, 그것으로 부터 실행하는 로직이 필요하다는 뜻
    - ★거리는.. 이전 단계에 비해서 거리가 늘었나를 판단해서 집어넣는 식으로
        - 이 아이디어는 자주 나오는 아이디어인데 걸핏하면 잊어먹음 주의!
'''

# BFS 선언, 문제의 조건 상 BFS는 한 곳이 아니라 여러 시작점에서 동시 실행하는 경우가 있을 수 있다
# 큐의 방문 처리 방식에 주의! 큐에 넣기 전에 먼저 방문처리 부터 해야함.
def BFS_tomato(spot_1_lt):

    # 방문처리
    queue=deque(spot_1_lt) # 튜플로 큐를 넣어 줌
    max_value=0
    while(queue):
        pr,pc=queue.popleft()
        # 방향 탐색하면서 훑어본다.
        for k in range(4):
            nr=pr+dr[k]
            nc=pc+dc[k]
            if (-1<nr<N and -1<nc<M) and farm[nr][nc]==0:
                # 큐에 넣기 전에 방문처리
                farm[nr][nc]=farm[pr][pc]+1
                queue.append((nr,nc))

        # 확인용
        '''for line in farm:
            print(line)
        print("\n")'''
        if len(queue)==0:
            max_value=farm[pr][pc]-1
    return max_value

from collections import deque
import sys
input=sys.stdin.readline
M,N=map(int,input().split()) # N: 행, M: 열 (착각하지 않게 주의)

# 결과출력
result=-1

# 창고
farm=[]
what_lt=[0 for _ in range(1001)]
# 방향벡터: 동서남북
dr=[0,0,1,-1]
dc=[1,-1,0,0]

for _ in range(N):
    farm.append(list(map(int,input().split())))

# 초기 1인 지점 탐색
spot_1_lt=[]

for row,line in enumerate(farm):
    for col,value in enumerate(line):
        if value==1:
            spot_1_lt.append((row,col))

# 토마토 BFS Search
result=BFS_tomato(spot_1_lt)

# 0이 있는지 탐색
for row,line in enumerate(farm):
    for col,value in enumerate(line):
        if value==0:
            result=-1
            break

print(result)