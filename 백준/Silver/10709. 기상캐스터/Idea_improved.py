'''
[아이디어]
1. 우측으로 j를 +1 증가시키면서 c를 만나면 cnt=0
else 면 cnt를 증가 시킴
2. 그런데 cnt를 무조건 증가시키지는 않는다. 구름이 없다면
cnt!=-1일때 즉, cnt가 0보다 클때 증가시키기.

3.카운트는 매 line 한번 돌고나면 -1로 초기화
'''

import sys
input=sys.stdin.readline

H,W=map(int, input().split())
arr=[input() for _ in range(H)]
v=[[0]*W for _ in range(H)]

for i in range(H):
    cnt=-1 # 'c' 만나지 못하면 계속 -1
    for j in range(W):
        if arr[i][j]=='c': # 구름을 만나면 0으로 초기화
            cnt=0
        else:
            if cnt>=0:
                cnt+=1
        v[i][j]=cnt

for lst in v:
    print(*lst)
