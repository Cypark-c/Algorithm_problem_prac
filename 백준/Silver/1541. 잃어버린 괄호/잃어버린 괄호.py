'''
[아이디어]
괄호를 통해 식의 값을 최소로 만들기
어떻게 하면 최소가 되나?→최대한 음의 값이 되도록

1. 최대한 음의 값이 되려면, - 뒤에 있는 수를 매우 크게 만들어야함.
2. - 뒤에 +가 붙는건 상관이 없는데, -뒤에 -가 붙으면 그건 문제가 됨.
    - 그렇다면 -기준으로 split을 하는게 좋지 않나
    - 예시:
        1. 55-50+40 → 55-(50+40)
        2. 55-50+40-30 → 55-(50+40)-(30)
        - 이렇게 되면, -외의 기호라면 그냥 두면 되고 -가 나올때만 괄호를 열고 닫으면 됨
        - '-'를 만날때 괄호의 처리
            - '-' 바로 뒤에 '(' 괄호를 넣음.
            - 다른 '-'를 만나면 ')'괄호를 넣고 동시에 '('를 넣음
            - 그런데 사실 위와 같이 복잡하게 처리 안하고 그냥 split 선에서 끝낼 수 있을 듯.

이게 실버 2인 이유가 파이썬이 문자열 처리가 쉬워서 그러지 않을까
'''

import sys
input=sys.stdin.readline().rstrip()
A=list(input.split('-'))
#print("변환 전 리스트:",A)
for i in range(len(A)):
    item_lt=A[i].split('+')
    for j in range(len(item_lt)):
        item_lt[j]=int(item_lt[j])
    A[i]=sum(item_lt)
#print("변환 후 리스트:",A)
result=A[0]
for i in range(1,len(A)):
    result-=A[i]
print(result)