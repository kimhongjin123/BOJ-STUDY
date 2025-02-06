n=[]
for i in range(3):
    n.append(input())
    if n[i].isdigit():
        n[i] = int(n[i])

for i in range(3): 
    if type(n[i])== int:   
        answer = n[i]-i+3
        break
if answer%3 == 0 and  answer%5 == 0:
    print("FizzBuzz")
elif answer%3== 0:
    print("Fizz")
elif answer%5 == 0:
    print("Buzz")
else:
    print(answer)