def hello():
    print('hello world')
hello()

def add(a,b) :
    print(a + b)
add(3,6)

def sub(a, b):
    """
    :param a:  integer
    :param b: onteger
    :return: nothing 화면에 보여줌
    """
    print()

def add(a,b ):
    return a+b

def not_ten(a):
    if a != 10:
        return
    print('10이 아님')

not_ten(20)
not_ten(30)
# return value 가 없을 때 - void
#
# gr = map(int, input().split())
# def grade(score):
#     if score >= 90 :
#         gr = 'A'
#         print('A')
#     elif score >= 80 :
#         gr = 'B'
#         print('B')
#     elif score >= 70 :
#         gr = 'C'
#         print('C')
#     elif score >= 60 :
#         gr = 'D'
#         print('D')
#     else :
#         gr = 'F'
#         print('F')
#     return gr

# 보다 return을 쓰면 된다
# 그럼 아래로 굳이 안내려 가도 되니까 괜찮다.
# def grade(score) :
#     if score >=90:
#         return 'A'
#     if score >= 80:
#         return 'B'
#     if score >= 70:
#         return 'C'
#     if score >= 60:
#         return 'D'
#     return 'F'

def add_sub(a, b):
    return a+b, a-b
x,y = add_sub(a,b)
print(x)
print(y)