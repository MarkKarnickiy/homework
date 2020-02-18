a = 2
b = 0
day = 1
while a < 3:
    a = a + b
    b = a * 0.1
    print('{}й - День: {}'.format(day,("%.2f" % a)))
    day = day + 1



