'''
[아이디어]
- 남의 코드를 보고 알았기 때문에 복습이 필요함.
- 해당 문제에서 BFS를 탐색할때 숫자를 늘려나간다는 방식으로 접근이 가능하다는 것도 중요한 스킬인듯.
- DFS 방식으로도 풀어봐야함
'''

def BFS(i,j,miro):
    queue=deque([(i,j)]) # 이렇게 선언을 해야 한번에 나옴. [] 이 부분이 필요함 잘 기억

    while queue:
        x,y=queue.popleft()

        # 방향탐색
        for i in range(4):
            nx=x+dr[i]
            ny=y+dc[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    return miro[N-1][M-1]

from collections import deque
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
miro=[]
# 미로 초기화
for _ in range(N):
    line=list(map(int,input().rstrip()))
    miro.append(line)
# 행, 열 방향벡터
dr=[1,0,-1,0]
dc=[0,1,0,-1]
print(BFS(0,0,miro))
