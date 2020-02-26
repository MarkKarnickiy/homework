a = float(input("Ведите делимое: "))
b = float(input("Введите делитель: "))
if b == 0:
    print("Деление на 0 это философия , а не число!")
else:
    my_func = lambda num1,num2:num1/num2
    print(f"Частное - {my_func(a,b)}")