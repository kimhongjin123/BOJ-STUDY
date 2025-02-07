n=[]
for i in range(3):
    n.append(input())   
    if n[i].isdigit():   #정수형으로 변환이 가능하면 정수로 변환해주기기
        n[i] = int(n[i])

for i in range(3):          #답인 숫자 구하기기
    if type(n[i])== int:   
        answer = n[i]-i+3
        break

if answer%3 == 0 and  answer%5 == 0:   #답인 숫자를 FizzBuzz형태로 변환
    print("FizzBuzz")
elif answer%3== 0:
    print("Fizz")
elif answer%5 == 0:
    print("Buzz")
else:
    print(answer)