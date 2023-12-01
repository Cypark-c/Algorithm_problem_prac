'''
[아이디어]
'-'는 행으로 이웃해야 만같음
'|'는 열로 이웃해야만 같음
인접한 것을 연속으로 찾아나간다는 것에 있어서 BFS, DFS 등을 사용하면 될 것 같음
방문한 경우는 'x'로 방문 표식을 두어 진행하지 않도록 함
N이 행, M이 열임에 주의! 
쉬워야 하고, 아이디어도 금방 떠오르긴 했는데 구현할 때 오랜만에 풀어서 그런지 몰라도 생각만큼 잘 되지가 않았음..
'''


# 어떤 문자를 받는냐에 따라 탐색 방법이 달라짐
def DFS(i,j):
    global count
    # 종료조건 이미 방문한 경우는 재방문 하지 않음
    if map[i][j]=='x':
        return

    if map[i][j]=='-':
        map[i][j] = 'x' # 방문표시
        if j+1>=M:
            count+=1
            return
        else:
            if map[i][j+1]!='-': # 여기서 실수 할 수 있음,,
                count+=1
                return
            else:
                DFS(i,j+1)

    elif map[i][j]=='|':
        map[i][j] = 'x'  # 방문표시
        if i+1>=N:
            count+=1
            return
        else:
            if map[i+1][j]!='|':
                count+=1
                return
            else:
                DFS(i+1,j)
    return

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
map=[]
for _ in range(N):
    map.append(list(input().rstrip()))
# print(map)

count=0 # for count Floor
for i in range(N):
    for j in range(M):
        DFS(i,j)
    #for item in map:
        #print(item)
    #print(count)
    #print("\n")
print(count)