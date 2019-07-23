
# def 함수이름(매개변수=값):
#     코드
# ---------- 초기값 지정하기
def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
# --------------초기값 지정되어 있더라도 값을 넣으면 해당 값이 전달됨
personal_info('홍길동',40, '서울시 용산구 이촌동')

#----------------초기값 지정된 매개변수의 위치\
 # 초기값이 없는 매개변수 올 수 없다.\
#
# def personal_info(name, address='비공개',age):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)
#
# SyntaxError: non-default argument follows default argument

# def personal_info(name, age, address = '비공개'):
#     print('이름',항열)

# 초기값 지정된 매개변수는 뒤쪽으로 몰아주기

def personal_info(name='비공개', age=0, address='비공개'):
    # 매개변수에 초깃값 지정시
personal_info()
# 인수를 안넣어도 호출 가능

# $$$$$$$$$$$$$$$$$$$$$$$$$$$
# 함수와 *를 리스트에 사용하고 **는 딕셔너리에 사용한다
# $$$$$$$$$$$$$$$$$$$$$$$$$$$