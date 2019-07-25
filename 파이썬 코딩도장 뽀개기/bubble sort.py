# sort중 가장 이상한 아이
# - 어렵지만 잘되고 멍청하지만 가장 기본적인 아이
alist = [5,4,21,3,15]
for i in range(len(alist)-1) :
    for k in range(i+1, len(alist)):
        if alist[i] > alist[k]:
            alist[i],alist[k] = alist[k],alist[i]
print(alist)
