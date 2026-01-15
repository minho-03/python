# 안녕하세요 10번 출력하기
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

# while문으로 "안녕하세요" 10번 출력하기
i = 0
while i < 10: # 조건을 만족하는 동안 반복
    print("안녕하세요")
    i = i + 1

# 1부터 10까지 출력하기
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# while문으로 1부터 10까지 출력하기
i = 1
while i <= 10:
    print(i)
    i += 1 # i=i+1

# 숫자 1부터 10까지 합 구하기
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
sum = sum + 4
sum = sum + 5
sum = sum + 6
sum = sum + 7
sum = sum + 8
sum = sum + 9
sum = sum + 10
print("1부터 10까지의 합:", sum)

# while문으로 합 구하기
num = 1   # 더할 숫자
sum = 0   # 합계를 저장할 변수

while num <= 10:
    sum = sum + num
    num += 1

print("1부터 10까지의 합:", sum)

# 1부터 20까지 숫자를 더한다
# 합이 100을 넘으면 while문을 종료한다
num = 1
hap = 0

while num <= 20:   # 1~20까지 반복
    hap += num
    if hap > 100:   # 합이 100을 넘으면 종료
        break
    num += 1

print("마지막 더한 숫자:", num)
print("합계:", hap)

# 1부터 10까지의 숫자 중 홀수만 더한다
num = 1
hap = 0

while num <= 10:
    if num % 2 == 0:   # 짝수일 때는 건너뛴다
        num += 1
        continue # 아래 코드를 실행하지 않고 조건 검사로 이동한다
    hap += num
    num += 1

print("1부터 10까지의 홀수 합:", hap)

