n= int(input())
sum = 0 
sum2=0
for i in range(1,n+1,1):
    sum += i
    sum2 += i*i*i
    
print(sum)
print(sum*sum)
print(sum2)