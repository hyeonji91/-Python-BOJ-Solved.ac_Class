case = int(input())
for i in range(case):
    h, w, n = map(int, input().split(" "))
    num = int(n/(h))+1
    floor = n%(h)
    if(floor == 0):
        floor = h
        num =num-1
    if(num < 10):
        print(str(floor)+'0'+str(num))
    else:
        print(str(floor)+str(num))
