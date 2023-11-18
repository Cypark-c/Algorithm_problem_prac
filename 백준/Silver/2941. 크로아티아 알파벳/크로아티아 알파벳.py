'''
[아이디어]
- 일단 입력은, 한 글자씩 받게 될 것
    - 문제는 판단해야 하는건, 최소 2글자 or 3글자로 단위로 판단 필요할 때가 있음
    - 나머지 알파벳은 한글자 씩 셈
        - dz= 이런거를 좀 주의해야함. (z= ,dz= 이런 경우도 있고)
        - dzx, dz= 왼쪽은 3글자인데 오른쪽은 1글자.
나는 생각보다 시간이 좀 걸렸다.. ㅠㅠ
'''

import sys
line=sys.stdin.readline().rstrip()
count=len(line) # 초기 문자열의 길이
for i in range(len(line)-1):
    if line[i]+line[i+1]=='c=' or line[i]+line[i+1]=='c-' or line[i]+line[i+1]=='d-' or line[i]+line[i+1]=='s=' or line[i]+line[i+1]=='z=' or line[i]+line[i+1]=='lj' or line[i]+line[i+1]=='nj':
        count-=1
    elif i+2<len(line) and line[i]+line[i+1]+line[i+2]=='dz=':
        count-=1 # z= 에서 이미 카운트를 하나 줄여서 여기에선 한번만 카운트를 줄이면 된다.
print(count)