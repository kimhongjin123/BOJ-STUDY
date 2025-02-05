
num = int(input())
ls=[]
for i in range(1,num+1):
    cons=i+sum(map(int,list(str(i))))
    if num == cons:
        ls.append(i)
if not ls:
    print(0)

else :
    print(ls[0])

