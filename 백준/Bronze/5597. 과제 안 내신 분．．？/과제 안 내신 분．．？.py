students=[]
numlist=[i for i in range(1,31)]
for _ in range(28):
    x=int(input())
    numlist.remove(x)

numlist.sort()
print(numlist[0])
print(numlist[1])