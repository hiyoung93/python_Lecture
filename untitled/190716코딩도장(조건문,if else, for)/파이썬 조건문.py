# 반복문 - 1. a,b입력받고 a+b 출력프로그램작성
# 입력 - 테스트케이스 개수 T 입력 (0 < A, B < 10)
# 출력 -  Case #x: A + B = C, x는 케이스 번호, c = a+b


# 반복문 - 2. 별그리기
# 5이상 9 이하 홀수 입력받아 별출력 프로그램

line = int(input("Diamond 의 길이를 입력하세요(5~9) : "))
for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))
for y in range(line * 2-3, 0, -2):
    print((" " * ( (line * 2 - 1 - y) // 2 )) + "*" * y)

