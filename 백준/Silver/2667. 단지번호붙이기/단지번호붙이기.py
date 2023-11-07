'''
[아이디어]
1.상하좌우로 움직이면서 1을 찾는다.
2.초기 시작 위치는 행렬을 서칭하다가 1이 보이는 곳으로 한다 (방문하지 않았어야함)
3.1을찾아 탐색하는 순서는 동,서,남,북 순으로 한다. 방문을 이미 했다면 멈춘다.
4.방문한 위치는 -1로 표기하자. -1로 표기함과 동시에 cnt를 증가시켜준다.
5.더이상 갈 곳이 없다면 빠져 나온다.
6.더이상 갈 곳이 없는 케이스는 사방이 막혀있거나 다 찾았는데도 인덱스가 행렬 바깥인 케이스거나
7.벽이 다 막혔을때
DFS로 풀어보자
'''
import sys
input=sys.stdin.readline
N=int(input())
apart_map=[]

# 아파트 지도 초기화
for _ in range(N):
    u=list(map(int,input().rstrip()))
    apart_map.append(u)
# 동서남북
dr=[0,0,1,-1] # 행
dc=[1,-1,0,0] # 열
cnt=0
result=[]
def DFS(apart_map,x_pos,y_pos):
    apart_map[x_pos][y_pos]=-1 # 방문처리
    global cnt
    cnt+=1
    # print("x의 위치:", x_pos, "y의 위치:", y_pos, "카운트:", cnt)
    # DFS로 순회하도록 한다.
    # 동서남북 순으로 순회할 것이며 방문처리시에 행렬 바깥으로 빠져나가지 않게 해야함
    # 행렬의 바운더리를 벗어나면 당연히 조건문을 skip 하게됨
    if (y_pos+dc[0])<N and apart_map[x_pos][y_pos+dc[0]]==1:
        #print("동")
        DFS(apart_map,x_pos,y_pos+1)

    if (y_pos+dc[1])>-1 and apart_map[x_pos][y_pos+dc[1]]==1:
        #print("서")
        DFS(apart_map,x_pos,y_pos-1)

    if (x_pos+dr[2])<N and apart_map[x_pos+dr[2]][y_pos]==1:
        #print("남")
        DFS(apart_map, x_pos+1,y_pos)

    if (x_pos+dr[3])>-1 and apart_map[x_pos+dr[3]][y_pos]==1:
        #print("북")
        DFS(apart_map, x_pos-1,y_pos)
    return

for i in range(0,N):
    for j in range(0,N):
        if apart_map[i][j]==1:
            DFS(apart_map,i,j)
            result.append(cnt) # 최종카운트
            cnt=0

result.sort()
# 문제에서 요구하는 출력
print(len(result))
for item in result:
    print(item)