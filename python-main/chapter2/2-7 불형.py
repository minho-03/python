# 불 (boolean)
a = True    #참
b = False   #거짓

# 비교 연산자

# 60점 이상이면 시험 통과
score = 70
print(score >= 60)   # 합격
print(score < 60)    # 불합격

# 로그인 비밀번호 검사
password = 1111
print(password == 1234) # 비밀번호가 맞는지?
print(password != 1234) # 비밀번호가 틀린지?

# num이 짝수인지?
num = 10
mod = num % 2 # 0
print(num % 2 == 0)

# 논리 연산자

# 놀이기구 탑승 조건
# => 10살 이상이고 키가 140cm 이상이면 탑승 가능
age = 12        #나이
height = 140    #키
print(age >= 10 and height >= 140)

# 영화 관람 조건
# 15살 이상 이거나 보호자를 통반했으면 관람 가능
age = 12                #나이
with_guardian = True    #보호자 동반 여부
print(age >= 15 or with_guardian)

# 좌석이 비어있는지?
# not은 상태를 반대로 해석할때 사용한다
is_occupied = True #자리에 사람이 있음
is_occupied = False #자리에 아무도 없음
print(not is_occupied) # 비어 있으면 True
