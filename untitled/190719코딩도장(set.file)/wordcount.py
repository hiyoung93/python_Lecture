filename = input('파일 이름 > ')
wordsDict = dict()

with open(filename, 'r') as file:
    for line in file :
        linewords = line.replace('(,' ' ').replace(')',' ').replace(',', ' ')\
            .replace('.', ' ').split()
        # print(linewords)
        for word in linewords:
            count = wordsDict.get(word, 0)
            #print(count, end = ' ')
            if count == 0 :
                wordsDict.update(dict([(word, count+1)]))

import operator
wordList = sorted(wordsDict.items(), key = operator.itemgetter(1), reverse = True)
for i in range(10):
    print(wordList[i])