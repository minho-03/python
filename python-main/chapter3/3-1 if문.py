# 조건문
# if문: 조건을 판단하여 코드를 실행하는 문법

# 자동차 속도가 80km 이상이면 과속카메라에 찍히는 예제
car_speed = 70  # 현재 자동차 속도
if car_speed >= 80:
    print("과속카메라가 사진을 찍는다")

# pass: 조건은 만들었지만, 아직 실행할 내용이 없을 때 사용
car_speed = 70
if car_speed >= 80:
    pass

# else문: 조건을 만족하지 않는 경우를 함께 처리할 때 사용
car_speed = 70
if car_speed >= 80:
    print("과속카메라가 사진을 찍는다")
else: 
    print("주행을 계속한다")

# elif문: 여러 조건을 비교해야할 때 사용
car_speed = 70
if car_speed >= 100:
    print("사진 찍고 면허 정지")
elif car_speed >= 80:
    print("사진 찍고 벌금")    
else: 
    print("주행 계속")

# 잘못된 코드 - if문를 따로 여러번 사용
# 속도가 100km 이상이면 두 조건이 모두 참이여서 print가 두번 출력됨
# 결과가 하나만 나오길 바란다면 elif를 사용해야함
car_speed = 100
if car_speed >= 100:
    print("사진 찍고 면허 정지")

if car_speed >= 80:
    print("사진 찍고 벌금")


