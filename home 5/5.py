while True:
    with open('num.txt', 'r+') as file1:
        print(input("Введите числа разделяя пробелом: "), file=file1)
        s = file1.readline()
        a = list(map(int, s.split()))
        print(a)
        print(sum(a))
        choice = input("Введите Y для продолжения или N для завершения: ")
        if choice == "Y":
            continue
        if choice == "N":
            s = file1.read()
            a = list(map(int, s.split()))
            print(sum(a))
            break