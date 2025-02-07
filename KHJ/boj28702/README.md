# Baekjoon 28701 - FizzBuzz 문제 해결

## 문제 설명
- 세 개의 연속된 수 또는 Fizz, Buzz, FizzBuzz 중 일부가 주어졌을 때, 다음 수를 예측하는 문제.
- `Fizz`는 3의 배수, `Buzz`는 5의 배수, `FizzBuzz`는 15의 배수를 의미함.
- 주어진 입력을 바탕으로 다음에 올 값을 출력해야 함.

## 코드 해설
```python
a = [input() for _ in range(0,3)]  # 3개의 입력값을 리스트로 저장
b = [0, 0, 0, 0]  # 다음 숫자를 저장할 리스트

for i in range(0, 3):
    if i == 0:
        if not (a[1] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[0] = int(a[1]) - 1
        if not (a[2] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[0] = int(a[2]) - 2
    elif i == 1:
        if not (a[0] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[1] = int(a[0]) + 1
        if not (a[2] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[1] = int(a[2]) - 1  
    else:
        if not (a[0] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[2] = int(a[0]) + 2
        if not (a[1] in ['Fizz', 'Buzz', 'FizzBuzz']):
            b[2] = int(a[1]) + 1  

b[3] = b[2] + 1  # 다음 숫자를 예상
if not (a[2] in ['Fizz', 'Buzz', 'FizzBuzz']):
    b[3] = int(a[2]) + 1

# FizzBuzz 규칙에 따라 출력
if b[3] % 15 == 0:
    print("FizzBuzz")
elif b[3] % 3 == 0:
    print("Fizz")
elif b[3] % 5 == 0:
    print("Buzz")
else:
    print(b[3])
```

## 코드 설명
1. **입력 처리**
   - `a` 리스트에 3개의 입력을 저장.
   - `b` 리스트는 다음 숫자를 저장하기 위해 사용됨.

2. **숫자 예측**
   - `Fizz`, `Buzz`, `FizzBuzz`가 아닌 경우 해당 값을 이용해 이전 수를 계산.
   - 각 위치에 맞는 숫자를 예측하여 `b` 리스트에 저장.
   
3. **다음 숫자 계산**
   - `b[3]`에 다음 수를 저장.
   - `FizzBuzz` 규칙에 따라 출력 값을 결정.

## 코드 개선점
- **중복 코드 제거 가능** → `b` 리스트에 값을 할당하는 부분을 함수화할 수 있음.
- **가독성 향상** → `if` 문에서 중복된 조건을 간략화할 수 있음.
- **추론 로직 간소화 가능** → `b[3]`을 계산하는 과정이 다소 복잡하여 개선 가능.

## 시간 복잡도 분석
- 입력값이 항상 3개이므로 O(1) (상수 시간) 복잡도를 가짐.

