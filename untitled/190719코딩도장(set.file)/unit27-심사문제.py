import string

with open('wars.txt','r') as file:
    words = file.readline().split() # 공백기준 분리
    for word in words : # words안에 word찾기
        if word.find('c') >= 0: # 'c'찿기
            word = word.strip(string.punctuation) # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 없애기
            print(word)
