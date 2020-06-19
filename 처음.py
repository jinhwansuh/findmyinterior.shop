a = '\ 1,293949,000 원'
b = a.replace('\\','').replace('원','').strip().replace(',','')
print(type(b))
print(b)


def akk():
    a = 1
    b = 2
    return a, b

x, y = akk()

print(x, y)