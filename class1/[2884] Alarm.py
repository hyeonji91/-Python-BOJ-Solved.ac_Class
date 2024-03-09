h, m = map(int , input().split())
t = int(h*60 + m)
if(t >= 45):
    t =t-45
else:
    t = 24*60 - (45-t)
h = int(t/60)
m = t%60
print(str(h) + " "+str(m))
