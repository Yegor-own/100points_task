f = open('26 сложное.txt')
n = int(f.readline())
d = dict()
a = []
for i in f:
    s,t = i.split()
    a.append([s,int(t)])
for i in a:
    d[i[0]] = 0
for i in a:
    d[i[0]] += i[1]
mx = 0
mxnm = ''
mn = 10**10
for ky, val in d.items():
    if val < mn: mn = val
    if val > mx:
        mx = val
        mxnm = ky
print(mn,mxnm)
