a = str(input())
b = a.split('.') # tach chuoi tai dau cham
c = []
d = ''
for s in b :
    for i in s :
        s = s.replace('  ',' ') # 2 dau cach = 1 dau cach
    if s[0] == ' ' :
        s = s[1:]
    if s[len(s)-1] == ' ' :
        s = s[0:-1]
    s = s.capitalize() # viet hoa chu cai dau
    c = c.append(s) # them s vao list c
for x in c :
    d = d + '. ' + x
d = d[2:] + '.'
print(d)

