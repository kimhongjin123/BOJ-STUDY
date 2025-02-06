# FizzBuzz 문제 해결 및 코드 개선

## ✅ 코드 평가
1. **기능적으로 동작 가능**
   - 입력된 값에서 정수를 찾아 특정 연산을 수행 후 FizzBuzz 조건을 검사함.
2. **가독성 개선 필요**
   - 변수명이 직관적이지 않음.
   - `type()`을 사용한 체크가 불필요하게 복잡함.
3. **입력 처리 방식 개선 가능**
   - `input()`으로 받은 데이터를 `int`로 변환하는 과정에서 더 효율적인 방식 사용 가능.
4. **출력 로직 개선 필요**
   - `FizzBuzz` 조건을 맨 위에 두면 `Fizz`, `Buzz`를 별도로 다시 검사할 필요 없음.

---

## 🔧 개선된 코드
```python
n = []
for _ in range(3):
    val = input()
    if val.isdigit():
        n.append(int(val))
    else:
        n.append(val)  # 숫자가 아니면 그냥 문자열로 저장

for i in range(3):
    if isinstance(n[i], int):  # type(n[i]) 대신 isinstance() 사용
        answer = n[i] - i + 3
        break

# FizzBuzz 판별
if answer % 15 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)
```

---

## 🔹 개선 포인트
1. **`type()` 대신 `isinstance(n[i], int)` 사용**  
   - 더 직관적이고 가독성이 좋음.

2. **입력 변환을 더 직관적으로 변경**  
   - `isdigit()`로 숫자인 경우에만 `int`로 변환하여 리스트에 저장.

3. **불필요한 `n[i] = int(n[i])` 제거**  
   - `input()`을 받은 후 바로 변환하여 리스트에 저장하는 것이 효율적.

4. **출력 조건 개선**  
   - `answer % 3 == 0 and answer % 5 == 0`를 `answer % 15 == 0`으로 변경하여 조건 중복 제거.

이제 가독성이 더 좋아지고, 불필요한 연산을 줄여서 성능도 개선됨!

