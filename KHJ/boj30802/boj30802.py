a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
sum=0
for i in b:
    sum+= i//c[0]
    if i%c[0]>0:
        sum+=1
print(sum)
print(a//c[1],a%c[1])
