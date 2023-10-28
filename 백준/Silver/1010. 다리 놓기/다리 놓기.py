# 다리 만들기
'''
접근: 가로지르면 안된다는건, 순서가 꼬이면 안된다는 것과 동의어.
예를 들어 3개 7개 있다고 가정을 하면,
1 1
2 2
3 3
  4
  5
  6
  7
서쪽의 3번 다리는 3~7까지 선택 가능하고,..? 많이 보던건데 이거. 조합 아닌가
'''
# from itertools import combinations <- 이 도구는 사용하지 않는다. 시간 제한있음

def factorial(K):
    if K==0:
        return 1
    else:
        return K*factorial(K-1)

T=int(input()) # test case
for _ in range(T):
    N,M=map(int,input().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))