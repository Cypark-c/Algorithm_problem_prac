'''
[아이디어]
가까운 먹이를 찾기에 BFS로 생각할 수 있음
BFS로 입력할때 현재 위치를 아기상어의 위치로 입력하고 먹을 수 있는 포지션을 찾음
'''

# BFS를 탐색하며 먹이가 될 수 있는 후보들을 반환해야함
# 그 후보를 cand라고 하자
def BFS(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for idx in range(4):
            ii, jj = i + dr[idx], j + dc[idx]

            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                # 5. 간선은 상하 좌우지만 조건에 따라서 움직이기 때문에 조건을 상세하여야한다.
                if graph[x][y] > graph[ii][jj] and graph[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif graph[x][y] == graph[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])
                elif graph[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii, jj])

    # 6. 후보 리스트는 우선 순위가 있기 때문에 정렬을 사용할 수 있다.
    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))

from collections import deque
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

# 초기위치 설정
p,q=0,0
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            p,q=i,j
            break


# 방향벡터 설정
dr=[-1,0,0,1]
dc=[0,-1,1,0]

# BFS로 나온 것 중 맨 앞에 나온 물고기만 먹고 다시 BFS 해야함
size=2 # 초기 상어 사이즈
cnt=0
ate=0 # 얼마나 먹었나

while True:
    graph[p][q]=size # 이게 중요한데 갱신을 하지 않으면 잡아먹다가 포기해버림
    cand=deque(BFS(p, q))
    # 큐에서 하나 뽑았는데 위치가 없으면 이제 BFS해도 의미 없다는 것이니 break
    if not cand:
        break
    time,np,nq=cand.popleft()

    cnt+=time
    ate+=1


    if ate==size:
        ate=0
        size+=1
    graph[p][q]=0
    p,q=np,nq

print(cnt)
