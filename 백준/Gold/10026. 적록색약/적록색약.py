'''
[아이디어]
DFS로 풀어보자.
적록색약은 R=G이다. 일단 효율적인 풀이는 아닐 수 있지만, 바로 생각난 풀이는
매핑을 각각 따로따로 해주는 것이다.

'R','G','B' 이런식으로도 나누어져있음.
그리고 이게 탐색을 진행하다가 더 나아갈 수 없을 때는 구역이 추가 되었음을
알려주도록 리턴을 해야함.
'''

def DFS_N(i,j):
    if graph_N[i][j]=='D':
        return 0 # 이렇게 한 거에는 이유가 있음.... 왜 그냥 리턴이 아니고 0일까. 뒤에 나옴

    # 방문처리
    node=graph_N[i][j] # R or G or B)
    graph_N[i][j]='D' # 방문한 노드의 처리

    # for check!
    '''
    for line in graph_RGX:
        print(line)
    print(i,j)
    print("\n")
    '''

    for dir in range(4):
        nr=i+dr[dir]
        nc=j+dc[dir]
        # 행렬 범위를 초과하지 않고
        if (-1<nr<N and -1<nc<N):
            if graph_N[nr][nc]==node: # 같은 알파벳을 가질 때 행동
                DFS_N(nr,nc)
    return 1

def DFS_RGX(i,j):
    if graph_RGX[i][j]=='D':
        return 0 # 이렇게 한 거에는 이유가 있음.... 왜 그냥 리턴이 아니고 0일까. 뒤에 나옴

    # 방문처리
    node=graph_RGX[i][j] # R or G or B)
    graph_RGX[i][j]='D' # 방문한 노드의 처리

    # for check!
    '''
    for line in graph_RGX:
        print(line)
    print(i,j)
    print("\n")
    '''

    for dir in range(4):
        nr=i+dr[dir]
        nc=j+dc[dir]
        # 행렬 범위를 초과하지 않고
        if (-1<nr<N and -1<nc<N):
            if graph_RGX[nr][nc]==node: # 같은 알파벳을 가질 때 행동
                DFS_RGX(nr,nc)
    return 1

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N=int(input())
graph_RGX=[] # 적록색맹
graph_N=[] # 정상인

# 동서남북 방향
dr=[0,0,1,-1]
dc=[1,-1,0,0]

for _ in range(N):
    N_line=list(input().rstrip())
    RGX_line=[]
    for item in N_line:
        if item=='G':
            RGX_line.append('R')
        else:
            RGX_line.append(item)
    graph_N.append(N_line)
    graph_RGX.append(RGX_line)


district_N=0
district_RGB=0
for i in range(N): # 행
    for j in range(N): # 열
        district_N+=DFS_N(i,j)
        district_RGB += DFS_RGX(i, j)

print(district_N,end=' ')
print(district_RGB)