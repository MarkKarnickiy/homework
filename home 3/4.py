x = float(input("Введите число: "))
x = abs(x)
y = int(input("Введите степень: "))
my_func = lambda a,b:a**b
print(my_func(x,y))
i = 1
z = x
while i < y:
    z = z*x
    i = i + 1
print(z)