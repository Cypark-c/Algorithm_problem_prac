import sys
input=sys.stdin.readline
N=int(input())
number_list=[]
while True:
    try:
        number_list.append(int(input()))
    except:
        break
number_list.sort()
for i in range(len(number_list)):
    print(number_list[i])