# ---------------------------- 키워드 언패킹 사용 ---------------
# 위치 인수를 사용하는 함수를 만들고 호출하기

print(10,20,30)
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
# -------------언패킹 사용 ------------
print_numbers(10,20,30)
def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(10)
print_numbers(10,20,30,40)
x = [10]
print_numbers(*x)
y=[10,20,30,40]
print_numbers(*y)

# ------------------------가변인수 만들기
# def 함수이름(*매개변수):
#     코드
def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(10,20,30,40)
x =[10]
print_numbers(*x)
y=[10,20,30,40]
print_numbers(*y)

#---------------고정인수와 가변인수를 함께 사용하기
def print_numbers(a, *args):
    print(a)
    print(args)
print_numbers(1)
# 고정인수와 가변인수를 함께 사용할 때는 고정변수 지정후 매개변수에 * 붙이기


#--------------------------- 키워드 인수와 딕셔너리 언패킹 사용 -----------
def persnal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

# 매번 순서와 용도를 기억해야해서 불편하다, 키워드 인수 제공,
# 함수(키워드=값)
# 순서를 지키지 않고 넣어도 괜찮다.

x = {'name':'하영','age':34,'address':'서울시 강남구 역삼동'}
persnal_info(**x)

# 딕셔너리의 이름 개수를 똑같이 맞춰야 한다, 다른 딕셔너리를 넣으면 에러

# persnal_info(**{'old':32,'name':'하영','address':'서울시 강남구 역삼동 '})

# persnal_info() got an unexpected keyword argument 'old'
#  = persnal_info() 에는 'old'라는 함수가 없습니다

# ------------------ ** 을 두번 사용해야하는 이유
# 딕셔너리는 키:값 형태로 저장되어 있다.
x = {'name':'하영','age':34,'address':'서울시 강남구 역삼동'}
persnal_info(*x)
# x의 키 값이 출력됨 ** 을 두번 언패킹하여 사용한다

# --------------------- 키워드 인수사용해서 가변 인수 함수 만들기 --------
# def 함수이름(**매개변수):
#     코드

# 매개변수의 이름은 관례적으로 keyword arguments= kwargs
def personal_info(**kwargs):
    for kw,arg in kwargs.items():
        print(kw, ': ', arg, sep='')
# 값을 한 개 넣어도 값 추출가능
personal_info(name='하영')

# 키워드 인수를 사용하는 가변인수함수를 만들 수 있다.
# 호출시, 키워드 인수를 각각 넣거나 딕셔너리 언패킹을 사용하면 된다
def personal_info(**kwargs):
    if 'name'in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])
# in으로 딕셔너리 안에 특정 키가 있는지 확인

def personal_info(name, **kwargs):
    print(name)
    print(kwargs)

personal_info('홍길동')
# **kwargs가 고정 매개변수보다 앞쪽에 오면 안된다.
# 고정매개변수보다 앞쪽에 오면 안된다.
# 순서중 가장 뒤쪽에 오기

# ------------위치 인수와 키워드 인수 함께 사용하기
def custom_print(*args,**kwargs):
    print(*args, **kwargs)

custom_print(1,2,3, sep=':',end='')
# *의 갯수대로 뒤쪽에 사용하기