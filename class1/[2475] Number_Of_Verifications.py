a = map(int, input().split(" "))
result = 0
for num in a:
    result += num**2
print(result%10)
