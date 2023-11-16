'''
[아이디어]
- 1을 제외하고는 알파벳이 있음
- 전화를 걸기 위한 최소 시간
- 7이랑 9는 다른 번호랑 다르게 4자리
'''

import sys
input=sys.stdin.readline
word=input().rstrip()
second=0
# ord A: 65
for chrac in word:
    if ord(chrac)<=67:
        second+=3
    elif ord(chrac)<=70:
        second+=4
    elif ord(chrac)<=73:
        second+=5
    elif ord(chrac)<=76:
        second+=6
    elif ord(chrac)<= 79:
        second += 7
    elif ord(chrac)<=83:
        second+=8
    elif ord(chrac)<=86:
        second+=9
    else:
        second+=10
print(second)