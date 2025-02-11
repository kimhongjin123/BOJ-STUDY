a = list(map(int,input().split()))
a1=int(a[0]*a[1]/a[2])
a2=int(a[0]/a[1]*a[2])
if a1>=a2 :
    print(a1)
else :
    print(a2)
