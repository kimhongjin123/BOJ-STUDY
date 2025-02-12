N,M=list(map(int,input().split()))

All = [input() for i in range(0,N+M)]

H=All[:N]
S=All[N:]
T=set(H)&set(S)

print(len(T))
print("\n".join(sorted(T)))



    