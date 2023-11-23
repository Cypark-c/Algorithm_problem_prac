'''
[아이디어]
7,3 요세푸스 순열?
    2  3
  1      4
   7  6  5
<3,6,2,7,5,1,4>
조금 생각해보면 쉽게 내용 유추가 가능함.
계속 새로 만들어지는 원 기준으로 생각 할 수 있으니까.
그리고 큐 자료 구조를 생각하면 더 수월할 것 같다. 하나가 빠지면, 그 빠진 자리의 바로 다음 자리가
다음 사이클의 시작이기 때문 큐로 풀지 않아도 푸는 방법이 매우 많을 듯
그런데 정작 까다로운건 출력 형식이었던 것 같다.
간단한 문제인데 생각외로 생각을 해봐야..(배울게 있다는 뜻)
'''
from collections import deque
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
queue=deque([i for i in range(1,N+1)]) # deque 초기화
permut=[]
while(queue):
    for i in range(0,K-1):
        queue.append(queue.popleft())
    permut.append(queue.popleft())
print("<", end='')
for i in range(N): # 꼭 이렇게 해야만 하나
    if i==N-1:
        print(permut[i],end="")
        break
    print(permut[i],end=", ")
print(">")

