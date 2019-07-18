# 조건문-1, 연도 4의 배수, 100의 배수 아닐 때 또는 400의 배수
# ex) 2012년 4의 배수는 윤년, 1900년은 4의 배수, 100의 배수 윤년 아님
# 연도를 입력받아(input)윤년인지 아닌지 출력하는 프로그램

year = eval(input(' 이번년도 > '))
if (year % 4 == 0 and year % 100 != 0) or \
    year % 400 == 0 :
    print(year, '윤년')
else:
    print(year, '윤년X')

# 조건문 -2, 원래 일어나야하는 시간 보다 45분 앞서는 시간으로 변경하기
# 시각 입력(시와 분) 을 입력하면 -45분전에 맞춰야할 시간 알려주는 프로그램

# 조건문 - 3, a,b,c를 입력하고 두번째로 큰 정수를 출력하는 프로그램 작성
if a > b and a > c :
    if b > c:
        print(b)
    else:
        print(c)
# 조건문 - 4, a^2+ b^2 = c^2 피타고라스 수,a > b > c 이고 a + b > c
# a + b + c = 1000은 수를 구하시오
outerBreak = False
for a in range(1,333):
    if outerBreak:
        break
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b:
            continue
        if a**2 + b**2 == c **2:
            print(a, b, c, a+b+c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;
