import re
filename = input('파일 이름 > ')
wordsDict = dict()

with open(filename, 'r',encoding='utf-8') as file:
    for line in file :
        linewords = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',filename).split()
        print(linewords)
        for word in linewords:
            count = wordsDict.get(word, 0)
            #print(count, end = ' ')
            if count == 0 :
                wordsDict.update(dict([(word, count+1)]))

import operator
wordList = sorted(wordsDict.items(), key = operator.itemgetter(1), reverse = True)
for i in range(10):
    print(wordList[i])