'''
[아이디어]
단순히 단어를 뒤집으면 된다. 라인을 한 줄에 받은 다음에
이것을 스플릿으로 쪼개어 리스트에 담고 역순으로 출력
'''

import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    line=input().rstrip()
    reverse_word=list(line.split())
    print(f"Case #{i+1}:",end=' ')
    for j in range(len(reverse_word)-1,-1,-1):
        print(reverse_word[j],end=' ')
    print("")