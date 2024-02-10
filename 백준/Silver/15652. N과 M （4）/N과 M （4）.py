'''
[문제 내용]
- 1부터 N까지 자연수 중 M개를 골랐다.
- 같은 수를 여러 번 골라도 됨, 단 "비내림차순"
- 다만 한번 나온 배열이 또 나오는 건 안된다.

[아이디어]
- DFS로 선택하게 함.
'''

def DFS_B(count,Narr):
    if count==M:
        if Narr not in result:
            result.append(Narr)
        return

    # 이 로직이 append pop 방식으로는 안되는듯 함.
    # 이 단계에서 현재 가진 max원소 보다 큰 값만 넣어야 한다.
    for i in Nums:
        if Narr==[]:
            DFS_B(count + 1, Narr + [i])
        
        elif Narr!=[] and i>=max(Narr):
            DFS_B(count+1,Narr+[i])


import sys
input=sys.stdin.readline
N,M=map(int,input().split())

# 1~N까지의 수열을 담음
Nums=[i for i in range(1,N+1)]
result=[]
DFS_B(0, [])

for item in result:
    print(*item)