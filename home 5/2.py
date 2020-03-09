strfile = open("my_file.txt", "r")
x = strfile.readlines()
print(f"Всего строк - {len(x)}")
strfile.close()
strfile = open("my_file.txt", "r")
w = 0
while True:
    a = (strfile.readline()).split()
    w = w + 1
    print(f"Слов в {w} строке: {len(a)}")
    if len(a) == 0:
        print("Строки закончились")
        strfile.close()
        break