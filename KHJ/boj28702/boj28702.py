a = [input() for _ in  range(0,3)]
b= [0,0,0,0]
for i in range(0,3):
    if i == 0 :
        if not (a[1] == 'Fizz' or a[1] == 'Buzz' or a[1] == 'FizzBuzz'):
            b[0] = int(a[1])-1
        if not (a[2] == 'Fizz' or a[2] == 'Buzz' or a[2] == 'FizzBuzz'):
            b[0] = int(a[2])-2        
        
    elif i == 1:
        if not (a[0] == 'Fizz' or a[0] == 'Buzz' or a[0] == 'FizzBuzz'):
            b[1] = int(a[0])+1
        if not (a[2] == 'Fizz' or a[2] == 'Buzz' or a[2] == 'FizzBuzz'):
            b[1] = int(a[2])-1  

    else:
        if not (a[0] == 'Fizz' or a[0] == 'Buzz' or a[0] == 'FizzBuzz'):
            b[2] = int(a[0])+2
        if not (a[1] == 'Fizz' or a[1] == 'Buzz' or a[1] == 'FizzBuzz'):
            b[2] = int(a[1])+1         
b[3]=b[2]+1
if not (a[2] == 'Fizz' or a[2] == 'Buzz' or a[2] == 'FizzBuzz'):
    b[3]=int(a[2])+1


if b[3]%15 == 0:
    print("FizzBuzz")
elif b[3]%15 != 0 and b[3]%3 == 0:
    print("Fizz")
elif b[3]%15 != 0 and b[3]%5 == 0:
    print("Buzz")
else:
    print(b[3])
