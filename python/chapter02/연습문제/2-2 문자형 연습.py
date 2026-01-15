#1. "Hello" 와 "Python"을 +연산자로 연결해 출력하세요
print("Hello" + "Python")

#2. *연산자를 사용해 "야호"를 3번 출력하세요
print("야호" * 3)

#3. "멍"을 2번, "냥"을 3번 반복해 출력하세요
print("멍" * 2 + "냥" * 3)

#4. 인덱스를 사용해 문자열 "text"에서 첫번째 글자를 출력하세요
a = "text"
print([0])

#5. 인덱스를 사용해 문자열 "text"에서 마지막 글자를 출력하세요
a = "text"
print([-1])

#6. 문자열 "abcdefg"에서 슬라이스를 사용해 "abc"를 출력하세요
a = "abcdefg"
print(a[:3])

#7. 문자열 "abcdefg"에서 슬라이스를 사용해 "cde"를 출력하세요
a = "abcdefg"
print(a[2:5])

#8. 문자열 "abcdefg"에서 슬라이스를 사용해 "cdefg"를 출력하세요
a = "abcdefg"
print(a[2:])

#9. 문자열 "안녕하세요 반가워요"에서 슬라이스를 사용해 "안녕하세요"와 "반가워요"를 각각 출력하세요
a = "안녕하세요 반가워요"
print(a[:5])
print(a[5:])

#9. 문자열 "20260112Mon"에서 슬라이스를 사용해 연도, 월, 일, 요일을 각각 출력하세요
a = "20260112Mon"
print(a[:5])
print(a[4:6])
print(a[5:7])
print(a[6:8])
print(a[8:])

#10. 문자열 함수를 사용해 문자열 "programming"의 길이를 구하세요
a = "programming"
print(len(a))

#11. 문자열 "2026-01-12"에서 "-"를 "/"로 바꿔 출력하세요
a = "2026-01-12"
print(a.replace("-","/"))