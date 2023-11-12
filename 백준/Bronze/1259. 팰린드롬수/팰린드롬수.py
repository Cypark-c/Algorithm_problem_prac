'''
펠린드롬수
[아이디어]
1.문제에서도 주어졌듯이 데칼코마니.
12321 은 배열이 길이가 5
그냥 reverse해서 자기 자신과 같으면 끝 아닌가.
어렵진 않고 역순 출력은 기억해야함
'''
import sys
input=sys.stdin.readline
while(1):
    message=input().rstrip()
    if message=='0':
        break
    if message==message[::-1]: # 역순 출력
        print("yes")
    else:
        print("no")