a=1 
n=int(input())
s=1
for i in range(1,n+1,1):
    if s>=n:
        a=i
        break
    s+=6*i
print(a)