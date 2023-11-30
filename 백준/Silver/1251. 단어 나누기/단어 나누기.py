'''
[아이디어]
단어를 임의로 쪼개는데, i,j로 접근하면 될 듯
[복잡도]
O(n^2) but, 단어 길이가 짧음
'''
import sys
word=sys.stdin.readline().rstrip()
wr_lt=[]

for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        wr_lt.append(word[i-1::-1]+word[j-1:i-1:-1]+word[:j-1:-1])
wr_lt.sort()
print(wr_lt[0])