my_f = open("my_f.txt", "r")
while True:
    try:
        f = list(my_f.readline().split())
        x = float(f[1])
        if x < 20000:
            print(f)
    except IndexError:
        print("Работники закончились")
        break
