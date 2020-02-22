d = list(input("Введите элементы списка: "))
print(d)
if len(d) % 2 != 0:
    arr = d[-1]
    d.pop()
    d[::2],d[1::2] = d[1::2],d[::2]
    d.append(arr)
    print(d)
else :
    d[::2],d[1::2] = d[1::2],d[::2]
    print(d)