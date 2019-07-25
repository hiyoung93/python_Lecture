# ----------------------- 재귀 호출 사용하기
# def hello():
#     print('Hello, world!')
#     hello()
# print(hello())

# 최대 재귀 깊이를 초과하면 RecursionError가 발생

# -------------------- 호출에 따른 종료 조건 만들기
def hello(count):
    if count == 0:                      # 종료 조건만들기
        return                          # count가 0 이면 함수 호출 NO
    print('Hello, World', count)        #
    count -= 1
    hello(count)
hello(5)

# --------------- 재귀호출로 팩토리얼 구하기
def factorial(n):
    if n == 1:                  # n == 1 일 때
        return 1                # 1 반환하고 재귀호출을 끝냄
    return n * factorial(n-1)   # n 과 factorial 함수에 n-1을 넣어서 반환된 값 곱하기
print(factorial(5))

''' factorial 함수를 만들 때 매개변수 n을 지정한다.
    1~n까지 곱을 구하는 문제 , n 부터 1 씩 감소하는 재귀호출
    n == 1 이 되었을 때 재귀호출을 중단한다.'''
n = int(input())
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)       # n과 factorial 함수에n-1넣어서 반환되는 값 곱하기
