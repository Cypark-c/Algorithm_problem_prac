import sys
# 총 가진 바구니의 수, 공을 바꾸는 횟수
N,M=map(int,sys.stdin.readline().split())

# 바구니 초기화: 처음에는 바구니 번호의 공이 들어있는 것임
basket=[val for val in range(N+1)] # 0번째 인덱스는 버릴 것.

# 공 바꾸기
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i],basket[j]=basket[j],basket[i] #swap
string=''
for item in basket[1:]:
    string+=str(item)+' '
print(string)