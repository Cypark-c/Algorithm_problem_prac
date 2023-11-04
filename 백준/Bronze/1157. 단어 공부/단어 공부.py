# 코드가 좀 쓸데없이 긴데?
X=list(map(str,input())) # 문자열은 오히려 split을 안써야 개별적으로 받음
for i in range(len(X)):
    X[i]=X[i].upper() # 항상 주의해야 할게 인덱싱을 해야 배열은 접근이 됨.
#print(X)
table=list(set(X)) # 집합을 통해 고유한 알파벳만 남김.

max_item=X[0]
table_cnt=[]
for item in table:
    table_cnt.append(X.count(item))

#print(table)
#print(table_cnt)
K=max(table_cnt)
max_count_char=X[0]
for i in range(len(table)):
    if table_cnt[i]==K and table_cnt.count(K)==1:
        max_count_char=table[i]
        break
    else:
        max_count_char="?"
print(max_count_char)