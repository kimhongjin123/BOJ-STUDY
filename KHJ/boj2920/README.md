# Baekjoon 2920 - 음계 (Scale)

## 문제 설명
8개의 숫자로 이루어진 수열이 주어졌을 때, 이 수열이 오름차순(ascending), 내림차순(descending), 또는 섞여 있는지(mixed)를 판별하는 프로그램을 작성합니다.

## 입력
- 첫째 줄에 8개의 정수가 주어집니다. (각 숫자는 1 이상 8 이하이며 중복되지 않음)

## 출력
- 수열이 1부터 8까지 오름차순이면 "ascending" 출력
- 수열이 8부터 1까지 내림차순이면 "descending" 출력
- 그 외의 경우 "mixed" 출력

## 코드 구현 (Python)
```python
b=[i for i in range(1,9)]
c=[i for i in range(8,0,-1)]
a= list(map(int,(input().split())))

if a == b :
    print("ascending")
elif a == c :
    print("descending")
else :
    print("mixed")
```

## 코드 설명
1. 오름차순 리스트 `b`와 내림차순 리스트 `c`를 생성합니다.
2. 입력을 받아 리스트 `a`에 저장합니다.
3. 입력 리스트 `a`와 `b`, `c`를 비교하여 결과를 출력합니다.
   - `a`가 `b`와 같다면 "ascending" 출력
   - `a`가 `c`와 같다면 "descending" 출력
   - 그 외의 경우 "mixed" 출력합니다.

## 예제 입력 및 출력
### 예제 1
**입력:**
```
1 2 3 4 5 6 7 8
```
**출력:**
```
ascending
```

### 예제 2
**입력:**
```
8 7 6 5 4 3 2 1
```
**출력:**
```
descending
```

### 예제 3
**입력:**
```
8 1 7 2 6 3 5 4
```
**출력:**
```
mixed
```

## 시간 복잡도 분석
- 리스트 비교 연산은 `O(N)`이므로, 길이가 8로 고정된 문제에서는 매우 빠르게 실행됩니다.