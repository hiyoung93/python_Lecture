# ------------------------------------- 3번
a,b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if  i % 2 != 0:
         sum += i
print(sum)
# ------------------------------------ 4번
a = int(input('>'))
year = 0
while a < year :
    if year == a * 2:
        print(year)
# ----------------------------------- 5번
bts = ['RM','진','슈가','제이홉','지민','뷔','정국']

# 5-1
print(bts[-2])
# 5-2
print(bts[:1])
# 5-3
print(bts[5:])
# 5-4
print(bts[2:5])
# 5-5
print(bts[0:7:2])


# ------------------------------------ 6번
vege = {'가지': 800, '오이':600, '수박':15000, '호박':1000, '깻잎': 500}
vege = list(sorted(vege.items(),key=lambda k: k[1]))

for k,v in vege:
    print(k,':',v)
# ------------------------------------ 7 번
principal = 1000
rate = 0.05
numyears = 5
year = 1
while year == numyears :
    principal= principal * (1+rate)
    print(year,principal)
    year += 1

# ------------------------------------ 9 번
a = [1,3,5,7,9]
b = list(map(lambda x: x * x, a))
print(b)