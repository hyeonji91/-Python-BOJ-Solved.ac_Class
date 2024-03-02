num = int(input())
for i in range(num):
    time, word = input().split(" ")
    time = int(time)
    for j in range(len(word)):
        for k in range(time):
            print(word[j], end = "")
        print()
