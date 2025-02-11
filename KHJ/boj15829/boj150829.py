a=int(input())
b = list(input())
c=[(ord(i)-96) for i in b]
sum=0
for i in range(0,a):
    sum+=c[i]*31**i
print(sum%1234567891)   
