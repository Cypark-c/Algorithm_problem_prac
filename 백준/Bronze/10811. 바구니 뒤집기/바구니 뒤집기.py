# 바구니 총 N개 각 바구니 1~N까지 번호 순서대로 적혀있음
# M회 동안 역순으로 바꾸는 행위를 함.
# i~j번째 바구니를 매 시행마다 선택

import sys

N,M=map(int,input().split())
bkt=[i for i in range(N+1)] # 0번 인덱스는 걍 무시할 것임

for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    flag=i
    partlist=[bkt[x] for x in range(j,i-1,-1)]

    for item in partlist:
        bkt[flag]=item
        flag+=1
[print(bkt[i],end=' ') for i in range(1,N+1)]

# 이중 반복문 사용했는데 뭔가 마음에 안든다.