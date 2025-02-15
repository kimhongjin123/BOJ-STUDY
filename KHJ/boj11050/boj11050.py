N,K= list(map(int,input().split()))
answer=1
for i in range(N,0,-1) :
    answer*=i
    if i <=N-K :
        answer//=i
    if i <=K:
        answer//=i

print(answer)
