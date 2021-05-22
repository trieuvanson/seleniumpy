# Cho 2 chuỗi a = '', b =''. Nối chúng lại theo thứ tự

a = ['a','b','c','d','e']
b = ['1','2','3','4']
c = []

for i in range(len(b) if len(a) >= len(b) else len(a)):
    c+= a[i]+b[i]
''.join(str(i) for i in c)

