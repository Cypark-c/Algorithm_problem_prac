'''
[아이디어]
일단 추가 시간이 0.25 → dynamic 으로 접근해야함
1을 출력 0을 출력 각각 확인 해야함.

피보나치 수를 구하는데, 이를 구함과 동시에, f(1), f(0)이 몇 번 나오게 되는지를
같이 호출해야 할 것 같다. 이것도 값을 저장해서 구현 할 수 있을 것 같다.
처음에 보게 되면, 재귀로 풀지, DP로 풀지 DP로 푼다면 어떻게 해야할지 헷갈릴 수도 있다.
복습을 반드시 해야할 문제 같다.
'''

import sys
input=sys.stdin.readline
T=int(input())


def fibo_dyna(n):
    # 0,1 번째 피보나치 상태 초기화
    fibo_list[0][0] = 1 # 0번째 피보나치 수 (value)
    fibo_list[0][1] = 1 # 0번째 피보나치 호출 수
    fibo_list[0][2] = 0 # 1번째 피보나치 호출 수

    if n>=1:
        fibo_list[1][0] = 1 # 1 피보나치 수 (value)
        fibo_list[1][1] = 0 # 0번째 피보나치 호출 수
        fibo_list[1][2] = 1 # 1번째 피보나치 호출 수

    if n<=1: # 0번째와 1번째 피보나치 수는 카운트 수만 늘려주고 리턴하면 된다.
        return
    else:
        for i in range(2,n+1):
            fibo_list[i][0]=fibo_list[i-1][0]+fibo_list[i-2][0] # 피보나치 수의 값
            fibo_list[i][1]=fibo_list[i-1][1]+fibo_list[i-2][1]
            fibo_list[i][2] = fibo_list[i-1][2] + fibo_list[i-2][2]

    return

for _ in range(T):
    n=int(input())
    fibo_list = [[0, 0, 0] for _ in range(n + 1)]
    fibo_dyna(n)
    print(fibo_list[n][1],fibo_list[n][2])

# 풀어보니 괜찮은 문제임을 알 수 있었음