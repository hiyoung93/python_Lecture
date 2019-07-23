korean, english, mathematics, science = 100, 86, 81, 91
# 호출 할때 마다 인수갯수가달라졌다  => 가변 인수 함수 만들기
# 인수를 위치 인수에 넣기 => 가장 큰 수를 구한후 return으로 반환하기

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수: ', max_score)

max_score = get_max_score(english, science)
print('높은 점수: ', max_score)
