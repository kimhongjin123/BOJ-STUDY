cnt=0
answer = list()
while(1):
    tri= list(map(int,input().split()))
    tri.sort()
    if tri[2]**2 == tri[1]**2 + tri[0]**2:
        answer.append("right") 
    else:
        answer.append("wrong")
    if tri == [0,0,0]:
        break
    cnt+=1

for i in range(cnt):
    print(answer[i])