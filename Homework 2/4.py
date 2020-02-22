arr = list(input("Введите несколько слов, разделите из пробелом: ").split())
for i in arr:
    i = i[:10:]
    print(i)