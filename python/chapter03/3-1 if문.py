# if문 : 조건에 따라 코드를 실행하는 문법

# 자동차의 속도가 80km 이상이면
# 과속카메라가 사진을 찍는다
# if 조건을 만족하지 않으면 블록이 실행되지 않는다
# if 안에 코드를 작성할 때에는 tab 들여쓰기
car_speed = 100 #현재 자동차의 속도
if car_speed>=80:
    print("과속카메라가 사진을 찍는다")
    pass # 작성할 코드가 정해지지 않았을 때

# if~else문
# 조건식의 결과에 따라
# 블록이 하나만 실행된다!
car_speed = 200
if car_speed >=80: #조건을 만족했을 때
    print("과속카메라가 사진을 찍는다")
else:               #조건을 만족하지않았을 때
    print("주행을 계속한다")

#elif
car_speed = 150
if car_speed >= 100:
    print("사진 찍고 면허 정지")
elif car_speed >= 80:
    print("사진 찍고 벌금")
else:
    print("주행 계속")