#file_ = open("my_file.txt", "x")
#file_.close()
file_ =  open("my_file.txt", "a")
while True:
    text = input("Введите текст: ")
    print(text, file=file_)
    if text == "":
        file_.close()
        break