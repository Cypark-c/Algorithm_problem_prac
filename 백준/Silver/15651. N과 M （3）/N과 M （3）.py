'''
[조건]
- 같은 수를 여러번 골라도 됨
- 수열은 사전 순으로 증가해야함

[아이디어]
3 3
1 1 1
1 1 2
1 1 3
1 2 1
1 2 2 ...

- visit 같은 개념보다는 그냥 모두 출력할 수 있게 만들어야함
'''

def DFS(count,Narr):
    if count==M:
        # Narr.sort()
        print(*Narr)
        return
    
    # append와 pop을 쓰면 조금 빨라지나?
    for i in range(1,N+1):
        Narr.append(i)
        DFS(count+1,Narr)
        Narr.pop() 
        
import sys
input=sys.stdin.readline
# N은 숫자 M은 길이
N,M=map(int,input().split())
Nums=[i for i in range(1,N+1)] # 1~N까지 자연수
result=[]

DFS(0,[])


