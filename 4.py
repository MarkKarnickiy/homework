number = int(input("Введите целое число: "))
max = 0
while number > 0:
    num_1 = number % 10
    if num_1 > max:
        max = num_1
    num_2 = number // 10
    number = num_2
print("Максимальная цифра Вашего числа %s" % max)
