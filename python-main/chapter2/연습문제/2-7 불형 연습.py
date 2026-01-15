# 1. 나이를 저장할 변수를 선언하고 임의의 숫자를 대입하세요
# 나이가 40세 이하면 참이 나오도록 조건식을 작성하세요
my_age = 25
print(my_age <= 40)

# 2. 소지금을 저장할 변수를 선언하고 임의의 숫자를 대입하세요
# 소지금이 2000원 이상이면 참이 나오도록 조건식을 작성하세요
money = 2500
print(money >= 2000)

# 3. 비밀번호를 저장할 변수를 선언하고 임의의 문자를 대입하세요
# 비밀번호가 "abcde"이면 참이 나오도록 조건식을 작성하세요
password = "abcd"
print(password == "abcde")

# 4. 변수를 선언하고 임의의 숫자를 대입하세요
# 숫자가 홀수라면 참이 나오도록 조건식을 작성하세요
num = 11
mod = num % 2 #1
print(num % 2 == 1)

# 5. 나이를 저장할 변수를 선언하고 임의의 숫자를 대입하세요
# 나이가 13세 이상이고 19세 이하라면 참이 나오도록 조건식을 작성하세요
age = 15
print(age >= 13 and age <= 19)

# 6. 변수를 선언하고 임의의 숫자를 대입하세요
# 숫자가 50 < x < 100 범위에 포함되면 참이 나오도록 조건식을 작성하세요
x = 80
print(x > 50 and x < 100)

# 7. 다음 코드를 실행하지 말고, 각 조건식의 결과를 주석으로 작성하세요
x = 1
y = 5
result1 = True and False        # ?
result2 = (1 == 2) or (1 < 2)   # ?
result3 = not False             # ?
result4 = (x < y) or (x == y)   # ?

# result1 = True and False        # False
# result2 = (1 == 2) or (1 < 2)   # False or True → True
# result3 = not False             # True
# result4 = (x < y) or (x == y)   # True or False → True
