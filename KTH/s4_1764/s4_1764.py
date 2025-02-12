n,m = map(int,input().split())
not_hear = []
not_see = []
for i in range(n):
    not_hear.append(input())
for i in range(m):
    not_see.append(input())

k = list(set(not_hear) & set(not_see))
k.sort()
print(len(k))
for i in range(len(k)):
    print(k[i])