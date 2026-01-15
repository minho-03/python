# 1. 아래와 같이 리스트를 만들고 
# for문을 사용해 요소를 하나씩 출력하세요
fruits = ["apple", "banana", "cherry"]

for f in fruits:
    print(f)

# 2. 아래와 같이 리스트를 만들고 
# for문을 사용해 요소를 하나씩 출력하세요
mixed = [1, "apple", 3.14, True]

for m in mixed:
    print(m)

# 3. 아래와 같이 장바구니 리스트를 만들고 
# 예시와 같이 출력하세요
# 예: "장바구니에 사과가 담겼습니다"
items = ["사과", "바나나", "우유"]

for item in items:
    print(f"장바구니에 {item}가 담겼습니다.")

# 4. for문을 사용해 "hi"를 5번 출력하세요
for i in range(5):
    print("hi")

# 5. for문을 사용해 5부터 15까지 출력하세요
for i in range(5,16):
    print(i)

# 6. 아래와 같이 리스트를 만들고 
# 모든 값을 더해 합계를 구하세요
nums = [10, 20, 30, 40, 50]
total = 0
for n in nums:
    total += n
print("합:", total)
