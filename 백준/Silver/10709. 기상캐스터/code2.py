import sys

h, w = map(int, sys.stdin.readline().split())
weather = []
for j in range(h):
    a = sys.stdin.readline().strip()
    temp =[]
    for t in a:
        if t == 'c':
            temp.append(0)
        else:
            temp.append(-1)
    weather.append(temp)

for i in range(h):
    for j in range(w):
        if weather[i][j] == 0:
            for k in range(j + 1, w):
                if weather[i][k] == 0:
                    break
                weather[i][k] += k - j + 1

for i in range(h):
    print(*weather[i])
