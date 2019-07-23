with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1
    print(count)


# 파일 읽기모드로 'r'로 열기
# readlines 파일로 내용을 읽어서 리스트형태로 가져오기
# 10자 이하 판단할때 리스트반톡하며 단어길이 구하기