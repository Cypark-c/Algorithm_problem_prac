word = input().upper()
unique_word = list(set(word))

cnt = []

for i in unique_word:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(unique_word[cnt.index(max(cnt))].upper())

'''
set 사용하는 기술은 같은데
count에 카운팅한 만큼 적립을 해두고 마지막에 인덱스 메서드를 활용한다는 부분이 다르다.
즉, 인덱스 메서드에 대한 적용이 필요해 여러 문제를 풀면서 익혀봐야함.
'''
