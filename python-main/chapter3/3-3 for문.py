# 학생들의 시험 점수 리스트
scores = [90, 25, 67, 45, 80]

# for문으로 시험 점수를 하나씩 꺼내서 출력하기
# for 변수 in 리스트:
#   수행할 코드
for score in scores:
    print(f"{score}점입니다")

# 시험 점수 하나씩 꺼내서 합격인지 검사
for score in scores:
    if score >= 60:
        print(f"{score}점은 합격입니다")
    else:
        print(f"{score}점은 불합격입니다")

# range함수는 연속된 숫자를 만들어주는 함수로 for문 함께 자주 사용된다
# range(개수): 0부터 숫자가 생성됨
nums = range(10)    # 0부터 9까지 생성 
# range(시작, 끝)
nums = range(1,11)  # 1부터 10까지 생성

# for문으로 숫자 출력
for n in nums:
    print(n)

# for문으로 같은 문장 반복
for n in nums:
    print("안녕하세요")

# 폴더 안의 파일을 하나씩 확인한다
# 텍스트 파일(.txt)은 무시하고 이미지 파일만 처리한다
# continue: continue를 만나면 아래 코드를 건너뛴다
files = ["photo.jpg", "doc.txt", "image.png", "profile.jpg"] # 폴더 안의 파일 목록

for file in files:
    if file.endswith(".txt"):
        continue    # 텍스트 파일이면 아래 코드를 실행하지 않음

    print(f"{file} 파일을 이미지 처리합니다.")

# 책장에서 특정 제목의 책을 찾는다
# 책을 발견하면 찾기를 멈춘다
# break: break를 만나면 반복문을 종료한다
books = ["자바 기초", "파이썬 입문", "데이터 분석", "웹 개발"]

for book in books:
    if book == "파이썬 입문":
        print("책을 찾았습니다!")
        break
    print("아직 찾는 책이 아닙니다.")
