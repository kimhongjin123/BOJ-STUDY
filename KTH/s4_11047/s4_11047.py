n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
cnt=0
for i in range(n):
    if k == 0:
        break
    if coin[n-i-1] < k or coin[n-i-1]==k :
        div=k//coin[n-i-1]
        cnt += div
        k-=  div * coin[n-i-1]
print(cnt)