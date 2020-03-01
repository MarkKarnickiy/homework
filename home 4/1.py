from sys import argv
name_, a, b, c = argv
print("Имя скрипта: ", name_)
print("Выроботка в часах: ", a)
print("Ставка в час: ", b)
print("Премия: ", c)
zp = (float(a)*float(b)) + float(c)
print(f"Ваша ЗП составляет: {zp}")