korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    min_score = min(args)
    max_score = max(args)
    return print(min_score,',',max_score)

def get_average(**kwargs):
    average_score = sum(kwargs.values())/len(kwargs)
    return print(average_score)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

# 3행에서 함수를 만든다 - get_min_max_score
# 가장 낮은점수 높은 점수를 구한다
# get_average 함수는 평균 점수를 구하고 있다.
# 함수 두개를 만들어야 한다
# 인수 갯수 변경됨, 가변 인수 함수로 만들기
# 인수를 위치 인수에 넣고 있다.
