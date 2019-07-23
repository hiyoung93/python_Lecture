# ------------- 내장함수
a = [1,2,3,4]
length = len(a)
print(length)

summation = sum(a)
print(summation)
# 중복없이 재사용이 가능하다

# def 를 사용해서 정의함,
def add(x, y):    # ( ) -인자값(pamamiter)가 온다,인자의 갯수를 정함.
    n = x + y
    return n # 반환하는 값
l =len([1,2,3]) # length함수르 호출한 함수
c = add(30, 300) # add안에 있는 n을 호출한다.
print(c)

