# 1. 반복문을 사용해 "하이"를 3번 출력하세요
i = 0
while i < 3:
    print("하이")
    i += 1

# 2. 반복문을 사용해 "경고!"를 5번 출력하세요
i = 0
while i < 5:
    print("경고!")
    i += 1    

# 3. 반복문을 사용해 "연습을 1번 완료했습니다"부터
# "연습을 5번 완료했습니다"까지 출력하세요
i = 1
while i <= 5:
    print(f"연습을 {i}번 완료했습니다")
    i += 1

#
# 4. 반복문을 사용해 0부터 4까지 출력하세요
i = 0
while i < 5:
    print(i)
    i += 1

# 5. 반복문을 사용해 11부터 20까지 출력하세요
i = 11
while i <= 20:
    print(i)
    i += 1

# 6. 반복문을 사용해 5부터 1까지 출력하세요
i = 5
while i >= 1:
    print(i)
    i -= 1    

# 7. 반복문을 사용해 "*"를 5번 이어서 출력하세요
# 결과: "*****"
i = 0
result = ""

while i < 5:
    result += "*" # 문자열 누적
    i += 1

print(result)

#
# 8. 아래와 같이 리스트를 만들고 
# 반복문을 사용해 요소를 하나씩 출력하세요
lis = ['a','b','c','d','e']
i = 0
while i < 5:
    print(lis[i])
    i = i + 1

# 9. 아래와 같이 리스트를 만들고 
# 반복문을 사용해 요소를 하나씩 출력하세요
lis = [10, 20, 30]
i = 0
while i < 3:
    print(lis[i])
    i = i + 1

# 10. 아래와 같이 리스트를 만들고
# 반복문을 사용해 모든 요소의 합을 구하세요
lis = [12, 7, 34, 19, 5]
i = 0
hap = 0

while i < 5:
    hap = hap + lis[i]
    i += 1

print("모든 요소의 합:", hap)

# 11. 아래와 같이 리스트를 만들고
# 숫자(int, float) 타입인 값만 더한 결과를 구하세요 
# 결과: 45.5
lis = [10, "a", 30, "hello", 5.5, True]
i = 0
hap = 0

while i < 6:
    if(type(lis[i])==int or type(lis[i])==float):
        hap = hap + lis[i]
    i += 1

print(hap)
