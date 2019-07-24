korean, english, mathematics, science = map(int, input().split())

if ( 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= science <= 100):
    print('잘못된 점수')
else : (korean + english + mathematics + science) / 4 >= 80:
        print('합격')
if:
        print('불합격')
