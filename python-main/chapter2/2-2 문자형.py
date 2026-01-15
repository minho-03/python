# 문자열
a = "hello world" #큰따옴표
a = 'hello world' #작은따옴표

# 데이터의 타입을 확인하는 함수 type 
print(type(a))

# 숫자1과 문자1의 차이점
print('1' + '1')    #'11' +문자열 연결 연산자 
print(1 + 1)        #2    +더하기 연산자

# 형변환
int("1") # "1" -> 1
float("1.23") # "1.23" -> 1.23

# 이스케이프 문자
# 역슬래시 + 문자 조합
# 문자 그자체나 특수문자를 표현할 때 사용한다

# 여러줄 만들기
a = 'hello\nworld' 
# 탭 넣기
a = '\thello world'

# 문자열 연산자

# 문자열 연결하기
a = "hello"
b = " world"
a + b

# 문자열 반복하기
a = "python"
a * 2

# 연결연산자와 반복연사자를 사용해 동물소리 만들기
print("멍" * 3 + "!" )   # 멍멍멍!

# 문자열 인덱스
# 인덱스번호는 0부터 시작
a = "hello"
a[0] #문자열[인덱스번호]
a[1]
a[2]
a[3]
a[4]
a[-1] #

# 문자열 슬라이스 1
a = "hello world"
a[0:4] #'hello'
a[7:12] #'world'

# 문자열 슬라이스 2
a = "20260112Mon"
date = a[:8]
day = a[8:]
date #'20260112'
day #'Mon'
print(date, day)

# 내용은 같고 값만 달라지는 문장을 템플릿으로 만드는 방법
# 예: 저의 이름은 둘리입니다 / 저의 이름은 도우너입니다

# f 문자열 포매팅
name = '둘리'
age = 10
f'나의 이름은 {name}입니다'
f'나의 나이는 {age}입니다'

# 문자열 관련 함수들

# 문자열 길이 구하기 len
a = '안녕하세요'
len(a)

# 특정 문자의 위치 찾기 find(찾을문자) → 문자의 위치
# 입력값: 찾을 문자
# 나오는값: 문자의 위치 index
a = "python"
a.find('y') #1
a.find('a') #값이 없으면 -1 반환

# 특정 문자의 위치 찾기 index
a = "hobby"
a.index('y') #1
# a.index('a') #값이 없으면 에러남

# 문자열 교체 replace(교체대상, 새로운문자) → 새로운문자열
# 입력값: 교체대상, 새로운문자
# 나오는 값: 새로운문자열
a = "i like coffee"
a.replace("coffee", "tea") #i like tea

# 문자열 나누기 split
a = "i like coffee"
a.split()       #['i', 'like', 'coffee']
b = "a:b:c:d"
b.split(':')    #['a', 'b', 'c', 'd']

# 문자열 삽입 join
",".join('abcd')
'a,b,c,d'


#############################

# 문자열이 특정문자로 시작하는지 확인 startswith
a = "i like coffee"
a.startswith("i") #True
a.startswith("a") #False

# 문자열이 특정문자로 끝나는지 확인 endswith
a = "i like coffee"
a.endswith("coffee")    #True
a.endswith("tea")       #False

#############################

# 소문자를 대문자로 바꾸기 upper
a = "hi"
a.upper() #'HI'

# 대문자를 소문자로 바꾸기 lower
a = "HI"
a.lower() #'hi'

# 공백 지우기
a = " hi "
a.strip()  #양쪽 공백 제거 'hi'
print('\''+a.strip()+'\'')

# 문자 개수 세기 count
a = "hobby"
a.count('b') #2