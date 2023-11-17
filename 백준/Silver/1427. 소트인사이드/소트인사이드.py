'''
[아이디어]
자리수를 단순히 내림차순으로 정리?
'''
import sys
number=sys.stdin.readline().rstrip()
sr=sorted(number,reverse=True)
for item in sr:
    print(item,end='')