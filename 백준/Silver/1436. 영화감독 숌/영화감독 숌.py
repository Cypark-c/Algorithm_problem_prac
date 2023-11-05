# 일단 666이라는게 무조건 들어가야함.
N=int(input())
'''
모든 자연수를 순회하면서 666이 들어가기만 하면 됨 일단 그렇다는 것.
'''
cnt=0
number=666
while(1):
    if str(number).count("666"):
        cnt+=1
    if cnt==N:
        break
    number+=1

print(number)