import random as rd
count = 0

while True:
    a = rd.randint(1, 6)
    b = rd.randint(1, 6)
    print(a, b)
    count += 1
    if a + b >= 10:
        break
print('Total count = ', count)
