money,policy=map(int,input().split())
print(money//policy)
print(int(money-(money//policy)*policy))