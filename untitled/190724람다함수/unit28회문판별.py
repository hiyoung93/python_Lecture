# --------------------------------회문판별 문자열의 길이 ---------------------
#
# for i in range(len(word)//2):
#     if word[i] != word[-1 -i] :
#         is_palindome = False
#         break

# -------------------------------n gram 만들기 --------------------
text = 'Hello'

for i in range(len(text) - 1):
    print(text[i], text[i+1],sep='')
# n gram을 만들때 어디까지 반복을 할 것 인가

text = 'this is python script'
words =text.split() # 공백을 기준으로 리시트를 만들어줘!
for i in range(len(words)-1): # 문자열 길이 -1 까지 반복하겠다
    print(words[i], words[i])


# -----------------------------