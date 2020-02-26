
def my_func():
    name = input("Your name: ")
    surname = input("Your surname: ")
    birth = input("Year of birth: ")
    city = input("Current city: ")
    e_maile = input("Your e-maile:")
    phone = input("Your phone: ")
    infor = name +" " + surname +" " + birth+" " + city+" " + e_maile+" " + phone
    return infor
inf = my_func()
print(inf)