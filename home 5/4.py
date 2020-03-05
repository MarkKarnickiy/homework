
with open("en.txt", "r") as tr:
    en2 = open("en2.txt", "r+")
    try:
     while True:
       a = (tr.readline()).split()
       print(a)
       if a[0] == "One":
           a[0] = "Один"
       if a[0] == "Two":
           a[0] = "Два"
       if a[0] == "Three":
           a[0] = "Три"
       if a[0] == "Four":
           a[0] = "Четыре"
       print(a, file=en2)
       if not a:
           en2.close()
           break
    except IndexError:
        print("Все в порядке, так и должно быть.")