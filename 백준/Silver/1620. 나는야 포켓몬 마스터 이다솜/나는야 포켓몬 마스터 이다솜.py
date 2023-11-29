'''
[아이디어]
N: 포켓몬의 개수
M: 맞춰야 하는 문제의 개수
- 포켓몬은 첫글자만 대문자인데
    - 일부 포켓몬은 마지막 문자만 대문자: 이런 포켓몬 어디서 봤던 것 같은데? ㅋㅋㅋㅋ
- 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어짐
- 도감입력은 항상 1번부터 차례대로 들어감 →이 말은 그냥 입력하는거 자체로 번호를 안다는 것임
- 발견되지 않은 변종 포켓몬이 많아서 100000 정도의 포켓몬이 존재할 수도 있다는거.. (시간복잡도 크니까 dict를 쓰자)
'''
import sys
input=sys.stdin.readline
N,M=map(int,input().split())

# 도감 입력
DEX=dict()
DEX_num=['Nouse']

for i in range(1,N+1):
    name=input().rstrip()
    DEX[name]=i # 포켓몬 이름이 사전이고, 번호를 매핑시킴
    DEX_num.append(name)

for _ in range(M):
    cmd=input().rstrip()
    try: # 문자입력
        print(DEX[cmd]) # 숫자 출력
    except: # 숫자입력
        print(DEX_num[int(cmd)]) # 리스트까지 같이쓰면 될 것 같기도?