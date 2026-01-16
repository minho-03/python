# 학생들의 시험 점수 리스트
scores = [90, 25, 67, 45, 80]
# for문으로 시험 점수 하나씩 꺼내기
# for문: 리스트 요소를 하나씩 꺼내다가 
# 더이상 꺼낼 요소가 없으면 반복 종료
for score in scores:
    print(scores)
# while문으로 시험 점수 하나씩 꺼내기
i = 0
while i < 5:
    print(score)
    i = i + 1

# 시험점수가 60점 이상이면 합격
# 60점 아래면 불합격
scores = [90, 25, 67, 45, 80]
for score in scores:
    if score >=60:
        print(f"{score}점은 합격")
    else :
        print(f"{score}점은 불합격")

# for문을 사용해 안녕하세요 3번 출력하기
# 3번??
# range 함수 활용
# 반환값: 0부터 2까지 숫자를 담고 있는 range객체
nums = range(3)

#for 변수 in 리스트, 튜플, range객체
# 반복횟수: range의 크기 3번
for n in nums:
    print('안녕하세요')

# 폴더 안에 파일들 중에서 이미지 파일만 출력하기
files = ["photo.jpg", "doc.txt", "image.png","profile.jpg"]
for f in files:
    # 파일의 확장자가 .txt라면 출력을 건너뛴다
    # .startwith .endwith
    if f.endwith(".txt") == True:
        continue
    print(f)

# 책을 발견하면 찾는 행위를 중단한다
books = ["자바 기초", "파이썬 입문","데이터 분석","웹 개발"]
# break : 조건을 만족하면 반복문을 종료한다
for book in books:
    if book == "파이썬 입문":
        print("책을 찾았습니다.!")
        break
    print("책을 찾는 중입니다..")