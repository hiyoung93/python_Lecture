# -------------------------- 리스트 할당 ' = '사용
a = [3,3,4,5,5]
b =a
print(a is b)
b[2] = 99
print(a)
print(b)
# -------------------- 리스트의 복사 -------copy
# copy 별개의 기억장소에서 움직이는 아이들
a = [20,3,4,5,6]
b = a.copy()
print(a is b)
print(a == b)

# -----------------------------------------for문 으로 요소 출력
# for 변수 in 리스트 :
#     반복 코드
#
a = [3,4,5,6,7]
for i in a:
    print(i)
# a 에 있는 요소를 꺼내면서 i 에 저장, 꺼낼때 마다 코드 반복
# print로 i출력 함, 리스트를 직접 지정해도 상관 없다.

# ------------------------------------인덱스와 요소 함께 출력 for 인덱스, 요소 in enumerate(리스트):
# enumerate에 리스트를 넣으면 for반복문에서 인덱스랑 함께 꺼내 올 수 있다.
a = [345,6,7,3,4,4]
for index, value in enumerate(a):
    print(index, value)
# index를 1 부터 꺼내 올 수도 있다.  :  print(index+1, value)
for index, value in enumerate(a):
    print(index+1,value)
# 조금 더 파이썬 스러운 방법  : for 인덱스, 요소 in enumerate(리스트, start = 숫자):
for index, value in enumerate(a, start =1):
    print(index,value)

# ------------------------ for문 인덱스요소 출력하기
a = [[34,5],[6,7],[3,2]]
for i in range(len(a)):
    print(a[i])
# + i엔 요소가 아닌 0부터 마지막 인덱스까지 인덱스가 들어간다.

#------------------------------- while 반복문으로 요소 출력
a = [34,5,4,2,21,5]
i = 0
while i < len(a):
    print(a[i])
    i += 1
# while 반복문으로 리스트의 요소를 출력할 때는 변수 i를 인덱스를 활용, i = 0
# i < len(a) 처럼 i 가 리스트의 길이(요소 개수)직전 까지 반복
# while 반복문안에서 요소를 출력할땐 print(a[i])와 같이 리스트의 인덱스 부분에
# i를 지정하여 출력한다.
while i < len(a):
    print(a[i])
    i += 1
