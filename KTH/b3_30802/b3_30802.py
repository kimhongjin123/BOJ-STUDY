people = int(input())  #사람수 저장 
size = [0 for i in range(6)]

size = list(map(int,input().split())) #리스트에 사이즈별 수를 칸을나눠 저장
T,P = map(int, input().split())

count = 0
for i in range(6):   
    count += ((size[i]-1)//T) +1
print (count) 
count2 = people //P
count3 = people % P
print(count2, end=' ')
print(count3)