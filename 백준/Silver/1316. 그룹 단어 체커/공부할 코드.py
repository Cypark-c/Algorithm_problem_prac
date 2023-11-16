import sys

n = int(sys.stdin.readline().strip())

def check(string):

    visited = set()

    for i in range(len(string)):
        if string[i] in visited:
            return 0
        elif i > 0 and string[i-1] != string[i]:
            visited.add(string[i-1])

    return 1

answer = 0

for _ in range(n):
    string = sys.stdin.readline().strip()

    answer += check(string)

print(answer)
