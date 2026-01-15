# 정수만들기
#변수의 타입은 값을 넣는 순간 결정된다
a = 10
a = -10
a = 0
#print : 값을 출력하는 함수
#type : 자료형을 반환하는 함수
result = type(a) #자료형을 확인하는 함수
print(result) #int

# 실수
a = 3.14
result = type(a)
print(a)
print(result)

# 실수 2
a = 1.23
print(a, type(a))

# 사칙연산
print(7+3)
print(7-3)
print(7*3)
print(7/3)
print(7//3)
print(7%3)

# 형변환
# 숫자형 int float
print(type(1))
print(type(1.5))

# 파이썬에서 연산을 할 때는 두 항의 타입을 맞춰야한다(형변환 필요)
# 1 -> 1.0
float(1)
print(float(1))
# 1.0 -> 1
int(1.0)
print(int(1.0))