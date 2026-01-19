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

