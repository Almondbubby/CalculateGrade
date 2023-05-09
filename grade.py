filename = input()
a = ""
with open(filename) as f:
    for x in f:
        if "Raw Score" in str(x):
            v = x.split("	")
            print(len(v))
            print(v[1])
            a += v[1] + " "

a = a.strip()
b = a.split(" ")
num = 0
den = 0
for i in b:
    q = i.split("/")
    print(q)
    num += float(q[0])
    den += float(q[1])
print(num)
print(den)
