a = int(input())
for i in range(a):
    print(' '*(a-i-1),'*'*(2*i-1))
    if i == (a-1):
        print('*'*(2*i+1))
        for i in range(a - 1, -1, -1):
            print(' ' * (a - i - 1), ('*' * (2 * i + 1)))