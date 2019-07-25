# 1 번, 대칭수를 곱하여 가장 큰 대칭수는?


# 2 번,
# 3 번
# 시저 암호, 입력 : 화면에서 문자열과 n값
plain, n = input('암호화할 문자열과 N값').split()
plain = [C for C in plain]
n = int(n)
LETTER_A = ord('A')
LETTER_Z = ord('Z')
cypher = []
for letter in plain:
    if ord(letter) + n > LETTER_Z :
        cypher.append(chr(LETTER_A + ord(letter) + n - LETTER_Z - 1))
    else :
        cypher.append(chr(ord(letter)+ n))
print(''.join(cypher))
# 상수 만들기 숫자화 no! 먼말인지 못알아 듣겟으니 천천히 가자^_^;  ㅗ

##  unix grep명령어
word, filename = input('찾고자 하는 문자열과 파일명 > ').split()
lineNo = 1
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        if line in file(word) >= 0:
            print('%3d: '% lineNo, )

