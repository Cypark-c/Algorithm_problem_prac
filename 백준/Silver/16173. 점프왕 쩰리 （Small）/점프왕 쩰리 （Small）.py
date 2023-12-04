'''
[아이디어]
크기-N by N jump
그래프 입력 받아서 진행하면 되고 오른쪽, 아래 이렇게만 진행 가능.
현재 포지션에서 이동을 계속 하다가, [N-1][N-1]에 도달하면 종료,

1. 행이나 열을 벗어나면 진행 불가능으로 로직을 짜두기.
2. 현재 포지션 값이 -1이면 도달한 것 ([N-1][N-1])

당장은 Base case에서 리턴문이 종료되더라도 결국 마지막에 처음 시작한 함수의 리턴문이 이걸 덮어 쓸 수 있으므로
flag 변수를 도입해서 문제를 푸는 걸 시도. 더 좋은 방법이 있지 않을까

[주의]
방문처리를 너무 당연하게 생각해서 잊어버리고 있었는데 안하면, 우연히 겹치는 칸에서 미친듯이 돌아버리는게 DFS
'''
def move(i,j):
    global flag
    # 영역을 벗어났거나 이미 방문했다면 리턴
    if i<=-1 or i>=N or j<=-1 or j>=N or graph[i][j]==-2:
        return

    # Base case
    if i==j==N-1:
        flag=1
        return

    # procedure
    nr=i+graph[i][j]
    nc=j+graph[i][j]
    graph[i][j]=-2 # 방문처리

    # 아래로 이동하기
    if -1<nr<N and j<=N-1:
        move(nr,j)
    # 오른쪽으로 이동하기
    if -1<nc<N and i<=N-1:
        move(i,nc)
    return

import sys
input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
flag=0
move(0,0)
# print(flag)
if flag==1:
    print("HaruHaru")
else:
    print("Hing")
