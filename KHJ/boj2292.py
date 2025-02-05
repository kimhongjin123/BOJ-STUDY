num = int(input())
cnt = 1
floor = 1
while True:


    floor =floor + 6*(cnt-1)
    if num - floor <= 0 :
        break
    else :
        cnt+=1

print(cnt)
                                                              
                                                              