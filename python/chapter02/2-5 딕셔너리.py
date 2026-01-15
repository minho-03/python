# 딕셔너리 생성
# 이름, 연락처, 생일 속성을 가짐
person = {'name':'둘리',
          'phone' : '010-1234-1234',
          'birth' : '0113'}
# 이름 조회
print(person['name']) #둘리

# 추가
person['address'] = '인천' #딕셔너리에 해당 키 없음(추가)
# 수정
person['name'] = '또치' #딕셔너리에 해당 키 있음(수정)

# 둘리의 연락처 조회
print(person['phone'])

# 프로퍼티 삭제
# 둘리의 생일 삭제
del person['birth']
print(person)

# 딕셔너리 만들 때 주의사항
# 키는 중복될 수 없다
# 키로 사용할 수 있는 것:
# 정수, 실수, 문자열, 튜플
d = {'a': 123,'b': 456}
print(d) 