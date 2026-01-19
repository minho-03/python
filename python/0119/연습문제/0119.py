# 홀수, 짝수 판별하기
def is_odd(number):
    if (number % 2) == 1:
        return True
    else:
        return False

# 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

# 프로그램 오류 수정하기 1
input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = input1 + input2
print("두 수의 합은 %s입니다" % total)

