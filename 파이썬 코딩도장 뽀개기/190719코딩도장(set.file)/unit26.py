# 오늘은 제대로 해보자^_^
fruits = {'strawberry', 'grape','orange','pineapple','cherry'}
print(fruits)
fruits = {'orange', 'orange','cherry'}
print(fruits)
fruits = {'strawberry', 'grape','orange','pineapple','cherry'}
# print(fruits[2]) set여서 에러남
# 'orange'in fruits python console창에서 사용하기

a = set('apple')
print(a)
c = set()
print(c)
c = {} # 딕셔너리 만들어짐
print(type(c)) # class 'dict'
c = set() # 이런식으로 해야지 class 'set'이 나온다
# set을 사용하는 때를 잘 모르겠음
# a = frozenset(range(10)) - 집합연산, 메서드요소 추가, 삭제 연산 사용 불가
# print(a |= 9)
print(frozenset({frozenset({1,2}), frozenset({3,4})})) # frozenset 안에는 frozenset만 사용가능



