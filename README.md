# 백준 스터디

## 📌 스터디 소개
백준 알고리즘 문제를 꾸준히 해결하며 알고리즘 실력을 향상시키기 위한 스터디입니다. 본 저장소는 문제 풀이 코드와 해설을 공유하고, 협업을 원활히 진행하기 위해 운영됩니다.

## 🔥 커밋 가이드

코드를 커밋할 때 일관된 메시지를 유지하기 위해 다음 규칙을 따릅니다:

### 📌 기본 커밋 규칙
```
[문제번호] 문제 제목 - 해결 방식
```

**예시:**
```
[1000] A+B - 구현
[1010] 다리 놓기 - DP
[1234] 최단 경로 - 다익스트라
```

### 📌 추가 작업 시
```
[Docs] README 수정
[Refactor] 코드 리팩토링
[Fix] 버그 수정
[Test] 테스트 코드 추가
[Chore] 기타 작업
```

### 📌 커밋 상세 가이드
1. **한 문제당 하나의 커밋**을 원칙으로 합니다.
2. **의미 있는 변경 사항 단위로 커밋**하는 것이 좋습니다.
3. 커밋 메시지는 간결하지만 이해하기 쉬운 방식으로 작성합니다.
4. 커밋 메시지는 영어보다는 한글을 권장합니다.
## 📝 문제 풀이 기록 방식
각 사용자는 자신의 폴더에서 문제 풀이를 진행하며, 문제 풀이 기록을 다음과 같이 작성합니다:
```
/solutions
  ├── [사용자이름]
        ├── [문제번호호]
            ├── 1000_A+B.py
            ├── 1010_다리놓기.py
```

## 💡 ChatGPT를 활용한 코드 해설 요청 방법

ChatGPT를 이용해 풀이한 코드의 해설을 요청할 수 있습니다.

**질문 예시:**
```
다음은 백준 1000번 문제(A+B)에 대한 코드입니다. 이 코드의 동작 방식과 시간 복잡도를 설명해 주세요.

```python
# 1000번 A+B
A, B = map(int, input().split())
print(A + B)
```
```

또는 문제 요약과 함께 질문할 수도 있습니다:
```
백준 1010번 "다리 놓기" 문제는 조합을 활용하여 해결해야 합니다. 제 코드는 다음과 같습니다. 이 코드의 로직과 시간 복잡도를 설명해 주세요.

```python
from math import comb
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N))
```
```

추가로 개선할 점이나 더 나은 알고리즘이 있는지 물어보는 것도 좋습니다!

## 💻 VS Code를 통한 Git 사용 가이드

### 1. 저장소 클론
1. **VS Code를 실행**하고 `Ctrl + ~` 를 눌러 터미널을 엽니다.
2. 다음 명령어를 입력하여 저장소를 클론합니다.
```
git clone <저장소 URL>
```
3. 클론된 폴더를 VS Code에서 엽니다.

### 2. 브랜치 생성 및 이동
1. `Ctrl + Shift + P` 를 눌러 "Git: Create Branch" 를 검색하여 새 브랜치를 생성합니다.
2. 또는 터미널에서 아래 명령어를 입력합니다.
```
git checkout -b <브랜치명>
```

### 3. 코드 작성 후 변경 사항 확인
1. VS Code 좌측의 **소스 제어(Git)** 아이콘을 클릭합니다.
2. 변경된 파일이 목록에 표시됩니다.
3. 터미널에서 다음 명령어로도 확인할 수 있습니다.
```
git status
```

### 4. 변경 사항 스테이징
1. **소스 제어(Git)** 패널에서 변경된 파일을 선택하고 `+` 버튼을 눌러 스테이징합니다.
2. 터미널에서 아래 명령어로도 가능합니다.
```
git add .
```

### 5. 커밋
1. **소스 제어(Git)** 패널에서 커밋 메시지를 입력하고 `✔` 버튼을 클릭합니다.
2. 터미널에서 아래 명령어를 실행할 수도 있습니다.
```
git commit -m "[문제번호] 문제 제목 - 해결 방식"
```

### 6. 원격 저장소로 푸시
1. `Ctrl + Shift + P` 를 눌러 "Git: Push" 를 검색하여 푸시할 수 있습니다.
2. 또는 터미널에서 아래 명령어를 실행합니다.
```
git push origin <브랜치명>
```

### 7. 최신 코드 가져오기 (풀)
1. `Ctrl + Shift + P` 를 눌러 "Git: Pull" 을 검색하여 실행합니다.
2. 또는 터미널에서 아래 명령어를 실행합니다.
```
git pull origin main
```

### 📌 시각적 자료
Git 사용을 위한 GUI 활용법도 가능합니다:
- **소스 제어(Git) 패널**을 활용하여 변경 사항을 추적
- **깃 그래프(Git Graph) 확장 프로그램** 설치하여 브랜치 및 커밋 로그 시각화
- **GitLens** 플러그인으로 변경 내역 및 기여자 분석 가능

스터디원 간의 원활한 협업을 위해 위의 가이드를 참고하여 Git을 사용해 주세요! 🚀

