'''
[문제 내용]
- 1부터 N까지 자연수 중 M개를 골랐다.
- 같은 수를 여러 번 골라도 됨, 단 "비내림차순"
- 다만 한번 나온 배열이 또 나오는 건 안된다.

[아이디어]
- DFS로 선택하게 함.
- 반복문 내에서 기준을 잡는 방법도 있음 (그런데 사실 백트래킹 단위 함수를 잘 짰으면 이런걸 신경 쓸 필요가 있을까)
'''

def DFS_B(start,count,Narr):
    if count==M:
        result.append(Narr)
        return
    
    # start 쓰는 방식이 훨씬 나음
    for i in range(start,N+1):
        DFS_B(i,count+1,Narr+[i])


import sys
input=sys.stdin.readline
N,M=map(int,input().split())

# 1~N까지의 수열을 담음
Nums=[i for i in range(1,N+1)]
result=[]
DFS_B(1,0,[])

for item in result:
    print(*item)