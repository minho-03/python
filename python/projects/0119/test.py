scores = []

n = int(input("학생 수를 입력하세요: "))

for i in range(n):
    score = int(input(f"{i+1}번째 학생 점수 입력: "))
    scores.append(score)

# 1. 전체 학생의 평균 점수를 구하세요
# avg = 0
# avg = (scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5] + scores[6]) / 7
# print(avg)

def avg(scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)
result = avg(scores)
print(result)

# 2. 80점 이상인 학생 수를 구하세요
# count = 0
# for score in scores:
#     if score >= 80:
#         count += 1
# print(count)

def count(scores):
    count = 0
    for score in scores:
        if score >= 80:
            count += 1
    return count
result1 = count(scores)
print(result1)

# 3. 각 학생의 등급을 출력하세요
# 등급 기준: 90점이상-A 80점이상-B 70점이상-C 그외-D
# 출력 예시: “첫번째 학생은 C등급입니다”
# “두번째 학생은 B등급입니다”

# score = 0
# i = 0
# for score in scores:
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     else :
#         grade = 'D'
#     print(f"{i}번째 학생은 {grade} 입니다 ")
#     i += 1


def grade(scores):
    i = 0
    for score in scores:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else :
            grade = "D"

        print(f"{i}번째 학생은 {grade} 입니다")
        i += 1

grade(scores)
