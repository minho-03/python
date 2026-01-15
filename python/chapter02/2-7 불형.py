# 불형 만들기
a = True #참
b = False #거짓

# 불형 연산자
# 비교 연산자
# 시험점수가 60점 이상이면 통과
score = 70
print(score >= 60)

# 사용자 로그인시 비밀번호를 맞게 입력했는지?
# 둘리의 원래 비밀번호 : 1234
password = "1233"
password == 1234
print(password == "1234")

# 사용자가 입력한 숫자가 짝수인지?
num = 10
# 2로 나머지값을 구했을 때 0이면 짝수
mod = num % 2
# 나머지값이 0이면 짝수
print(mod == 0)

# 논리연산자
# 놀이기구 탑승 조건
# 사람의 나이가 10살이상이고
# 키가 140cm 이상이면 탑승 가능
age = 12
height = 150
# 두가지 조건을 모두 만족해야 탑승 가능!
print(age >= 10 and height>=140)

# 영화 관람 조건
# 사람의 나이가 15살 이상이거나 
# 보호자를 동반했으면 관람 가능
age = 12                #나이
with_guardian = True    #동반여부
# 변수명 규칙
# 단어가 복잡할 때는 스네이크 기법 사용
# 단어1_단어2
# 다른 언어에서 사용하는 기법에는 카멜케이스가 있음 예) withGuardian
print(age>=15 or with_guardian==True)

# 영화관이 특정 자리가 비었는지?
# True - 자리에 사람이 있다
# False - 자리에 아무도 없다(비었다)
is_occupied = True
# is로 시작하는 변수는 보통 boolean
print(not is_occupied)
# not은 boolean을 반대로