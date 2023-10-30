# 성의 크기
N,M=map(int,input().split()) # 가로가 M, 세로가 N

# 성의 상태
import sys
castle=[]
for _ in range(N):
    castle.append(sys.stdin.readline().rstrip())
# print(castle) # 성의 상태 확인 (경비원이 얼마나 있나)
'''
idea는 모든 행과 열이니까
처음 상태에서 가로세로 다 없으면 그 겹치는 지점에 경비원 배치를 해야함
우선은, 행을 탐색하면서, 'X'를 찾고 X가 없는 행을 추린 다음에,
X가 없는 행에서 추가하는 방법으로 가져가면 되지 않을까 싶음
'''
row_cnt=[0 for _ in range(N)] # 행 count
for i in range(N):
    for j in range(M):
        if castle[i][j]=='X':
            row_cnt[i]=1
            break

col_cnt=[0 for _ in range(M)] # 열 count
for j in range(M):
    for i in range(N):
        if castle[i][j]=='X':
            col_cnt[j]=1
            break

#print(row_cnt)
#print(col_cnt)

'''
 1 1 0 1 1 0 1 1
1
0    ?     t
1
0    ?     t
0    ?     t

'''
print(max([row_cnt.count(0),col_cnt.count(0)]))



'''
  0 1 0
1 a b a
0 c a c
0 c a c

'''