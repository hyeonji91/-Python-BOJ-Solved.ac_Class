a = int(input())
b = int(input())
c = int(input())
result = a*b*c
digit = [0 for i in range(10)]
for i in range(len(str(result))):
    digit[result%10] += 1
    result = int(result/10)
for i in range(10):
    print(digit[i])
