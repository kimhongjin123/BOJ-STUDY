repeat = int(input())
floor=[0 for i in range(repeat+1)]
room=[0 for i in range(repeat+1)]

for i in range(1,repeat+1,1):
    floor[i] = int(input())
    room[i] = int(input())

people = [[0 for j in range(15)] for i in range(15)]
for j in range(1,15,1):
    people[0][j]= j  #j는 0층의 사람 1호부터 저장 
for i in range(1,15,1): #apt 사람 2차원 리스트로 표만들기기
    for j in range(1,15,1):   #이러면 0호는 0명이라고 가정하기기  #1층 1호부터 사람저장장
        people[i][j] = people[i][j-1] + people[i-1][j]

for i in range(1,repeat+1,1):
    print(people[floor[i]][room[i]])