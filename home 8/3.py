class Error:
    def __init__(self, *args):
        self.list_ = []
    def my_input(self):
        while True:
            try:
                a = int(input('Вводите значения и нажимайте Enter - '))
                self.list_.append(a)
                print(f'Список - {self.list_} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Продолжить? Y/N ')
                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Процесс завершен'
                else:
                    return f'Процесс завершен'
try_except = Error(1)
print(try_except.my_input())