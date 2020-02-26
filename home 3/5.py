while True:
    text = input("Введите слово, или несколько слов разделенных пробелом: ")
    my_func = lambda a:a.title()
    print(my_func(text))