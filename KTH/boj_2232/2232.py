a= int(input())
k=1
k2 = k
n=[]
sum=0 

while(1):
    for i in range(len(str(a))):
            n.append(k2%10)
            k2=k2//10
            sum+=n[i]       
    if a == k + sum:
        print(k)
        break
    if k==a:
         print(0)
         break
    k+=1
    k2=k
    sum=0
    n.clear()