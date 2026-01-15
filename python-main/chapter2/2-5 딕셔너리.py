# 학생 정보를 담은 딕셔너리 생성
d = {'name': '둘리', 'phone': '010-1234-5678', 'address': '서울'}

# 값 꺼내기
print(d['name'])    #딕셔너리[key]

# 새로운 요소 추가
d['age'] = 20       #딕셔너리[key] = value

# 요소 수정
d['address'] = '인천'     

# 요소 삭제
del d['name']       #딕셔너리[key]

# 주의사항!
# key가 중복되면 마지막 요소를 제외한 나머지는 무시
d = { 1: 'a', 1: 'b' }
print(d)

# 키는 변경되지 않는 자료형만 사용 가능
# 정수,실수,문자열,튜플 (가능) 리스트,딕셔너리,set (불가능)


#############################

# 딕셔너리 관련 함수

d = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}

# 모든 키 조회
keys = d.keys()
print(keys, type(keys)) # dict_keys 객체는 리스트와 비슷하게 생겼지만 리스트는 아님

# 모든 값 조회
values = d.values()
print(values)

# 모든 키와 쌍 조회
items = d.items()
print(items)

# key로 value 꺼내기
d = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}
print(d.get('name'))
print(d['phone'])

# 해당 key가 딕셔너리 안에 있는지 확인
print('name' in d)
print('email' in d)
