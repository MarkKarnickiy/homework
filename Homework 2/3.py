m = input("Введите число месяца от 1 до 12: ")
arr = list("12 1 2 3 4 5 6 7 8 9 10 11".split())
my_dict = {12:"December",1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"Octpber",11:"November"}
if m in arr[0:3:]:
    print("Winter - " + str(my_dict.get(int(m))))
if m in arr[3:6:]:
    print("Spring - " + str(my_dict.get(int(m))))
if m in arr[6:9:]:
    print("Summer - " + str(my_dict.get(int(m))))
if m in arr[9:12:]:
    print("Autumn - " + str(my_dict.get(int(m))))
