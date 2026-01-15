# 문자열
# 특수문자를 사용하면 줄바꿈 가능
a = "hello \nworld"
print(a)
# 문장 안에 탭 넣기
a = "\t hello world"
print(a)

# 문자열 연산자
# 문자열 연결하기
a = "hello"
b = "world"
print(a + b) #helloworld

# 문자열 반복하기
print(a * 3) #hellohellohello

# 위에서 배운 연산자를 사용해
# "멍"을 3번 반복하고 그 뒤에 "!"를 붙여주세요
print("멍" * 3 + "!")

# 인덱스
a = "hello"
# 인덱스를 사용해서 특정 문자 꺼내기(인덱스는 0번부터 시작!)
# 문자열변수[번호]
print(a[0]) #h
print(a[1]) #e
print(a[2]) #l
print(a[3]) #l
print(a[4]) #o

# 문자열
a = "string"
# 'string' 중에서 'g' 꺼내기
print(a[5])

# 문자열
a = "users~"
# "users~"에서 "u"만 꺼내기
print(a[0])

# 문자열
a = "hello world"
# 음수 인덱스로 문자 꺼내기
# 마지막 문자는 무조건 -1
print(a[10])
print(a[-1]) #d

# 문자열
a = "hello world"
# "hello world"에서 "hello"만 꺼내고 싶다.
# 문자열변수[시작번호:끝번호]
# 끝번호는 포함 안 됨
# 공백도 문자
print(a[0:5])
print(a[6:11])

# 문자열
a = "20260112Mon" #날짜
# 날짜와 요일로 분리하기
date = a[:8] #처음부터 8전까지(시작번호생략가능)
day = a[8:] #8부터 끝까지(끝번호생략가능)
print(date, day)

# 문자열 포매팅
# 예 : 저의 나이는 10입니다
#      저의 나이는 20입니다
age = 10
print(f'저의 나이는 {age}입니다')

# 문자열이 사용할 수 있는 함수들
# int float str


# 자주 사용하는 함수들
# 사용방법
# 문자열의 길이 구하기
# 입력값: 문자열
a = "안녕하세요"
print(len(a))
# 문자열 안에서 특정 문자의 위치 찾기
# 입력값: 찾고자 하는 대상
a = "python"
print(a.find('a')) #찾는 문자가 없으면 -1 반환
# print(a.index('a')) #없으면 에러

#함수란?
# 남이 만들어 놓은 기능을 가져다 쓰는 것
# 예 : 산술연산, 문자열연산 등
# 함수의 사용법 이해하기!
# 방법 : 파이썬 공식문서, gpt ...

# 특정 문자 교체하기 
a = "i like coffee"
# 메뉴 변경! coffee -> tea
# 입력값 : 교체대상, 새로운 문자열
# 나오는 값 : 교체된 새로운 문자열
result = a.replace("coffee","tea")
print(result)

# 문자열 나누기
# i/like/coffee => 3개로 분리
# split : 공백을 기준으로 분리하는 함수
# 필수 입력값 : 없음
# 나오는 값 : 문자열 목록
a = "i like coffee"
result = a.split()
print(result)

a = "a:b:c:d"
# 이번에는 :콜론을 기준으로 자르기
# sep : str | None = None
# 분리하는 기준이 되는 문자
# 입력값이 없으면 => 기본값 " " 공백
# 필요하면 직접 입력
result = a.split(":")
print(result)

# 문자열을 중간에 삽입하기
# join
print(" ".join("abcd"))

# 문자열이 특정문자로 시작하는지 확인
s = "i like coffee"
# "i like coffee"가 "i"로 시작하는지?
# 입력값: 시작되는 문자열
# 나오는값: 맞으면 true 아니면 false
print(s.startswith("i"))

# 문자열이 특정문자로 끝나는지 확인
# "i like coffee"가 coffee로 끝나는지?
print(s.endswith("coffee"))
