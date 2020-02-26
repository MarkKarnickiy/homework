arr =[]
while True:
    numbers = (input("Введите последовательность чисел: ")).split()
    do = input("Введите enter, чтобы получить сумму чисел. Для выхода нажмите q: ")
    if do == "enter":
        for i in numbers:
            i = float(i)
            arr.append(i)
    if do == "q":
        for i in numbers:
            i = float(i)
            arr.append(i)
        break
    print(sum(arr))
print(f"Конечная сумма чисел равна: {sum(arr)}")
