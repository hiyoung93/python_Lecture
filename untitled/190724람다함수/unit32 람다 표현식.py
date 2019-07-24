# ------------------------- 람다 표현식 사용하기
# 표현식으로 함수 만들기

def plus_ten(x):
    return x+10
print(plus_ten(2))

# plus_ten함수를 람다 표현식으로 작성

lambda x:x +10
# 람다 표현식은 이름이 없는 함수를 만든다. = 익명함수(anontmous function)
plus_ten = lambda x: x+10
print(plus_ten(3))
# ------------------------------- lambda표현식 자체를 호츌하기
# ( lambda 매개변수들: 식)(인수들)
print((lambda x: x+10)(34))
# ------------------------------- 람다표현식 안에서는 변수 못만듬
'''변수 만들려면 바깥쪽에 따로 만들고 넣어야 한다.'''
y = 10
print((lambda x : x+y)(2))
# ------------------------------- 람다 표현식을 인수로 사용하기

def plus_ten(x):
    return x+10

list(map())








