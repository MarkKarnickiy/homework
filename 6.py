a = int(input("Введите начальное кол-во км.: "))
c = 0 #коэфициент увеличения результата на 10%
b = int(input("Введите конечноеное кол-во км., но не неньше 3-х: "))
day = 1
while a < b:
    a = a + c
    c = a * 0.1
    print('{}й - День: {}'.format(day, ("%.2f" % a)))
    day = day + 1

print(f"На {day}-й день, спортсмен достигает результата не менее {b}км.")



