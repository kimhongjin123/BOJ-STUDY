N,K= list(map(int,input().split()))
Coin=[int(input()) for _ in range(N)]

sum=0

for i in range(N-1,-1,-1):
    if K//Coin[i] > 0:
        num=K//Coin[i]
        sum+=num
        K=K-num*Coin[i]

print(sum)