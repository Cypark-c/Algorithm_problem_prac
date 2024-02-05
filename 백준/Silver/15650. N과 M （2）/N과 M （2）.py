# N과M (2)
'''
[아이디어]
1~N까지 자연수 중에서 중복 없이 M개 선택, 고른 수열은 오름차순!
1~4, 2개 선택 케이스
3 1 → 1 2 3
4 2 → (1 2) (1 3) (1 4) (2 3) (2 4) (3 4)

■ 선택을 할 때마다 원래의 선택지에서 소거하면 나머지가 남음
■ 이것의 길이가 M이 되었을때 출력을 한다.
'''

def DFS_Bt(count,N_arr):

    # 종료조건
    if count==M:
        N_arr.sort()
        if N_arr not in result:
            result.append(N_arr)
        return


    for i in range(1,N+1):
        # 아직 방문하지 않았다면
        if N_visit[i]!=1:
            N_visit[i]=1
            DFS_Bt(count+1,N_arr+[i]) # 길이 변형이 좀 문제
            N_visit[i]=0


import sys

input=sys.stdin.readline
N,M=map(int,input().split())

# 숫자
Nums=[i for i in range(1,N+1)]

# 방문노드 체크
N_visit=[0 for _ in range(N+1)]

# 결과 넣기
result=[]

DFS_Bt(0,[])
for item in result:
    print(*item)
