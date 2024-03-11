num = int(input())

for i in range(num):
    temp = 0 #중간 점수
    score = 0 #최종 점수
    test = input()
    for j in test:
        if(j == 'O'):
            temp = temp+1
            score = score + temp
        else:
            temp =0
    print(score)
