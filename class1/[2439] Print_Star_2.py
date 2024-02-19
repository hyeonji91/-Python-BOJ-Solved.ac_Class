num = int(input())
str =""
for i in range(num):
    str = ""
    for j in range(i+1):
        str += "*"
    print(str.rjust(num), end = "")
    print("")
