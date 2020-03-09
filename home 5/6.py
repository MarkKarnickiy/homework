file_ = open("text_6.txt", "x")
dict_ = {}
with open("text_6.txt") as j:
    for i in j:
        name, stats = i.split(':')
        sum_ = sum(map(int, "".join([el for el in stats if el == ' ' or (el >= '0' and el <= '9')]).split()))
        dict_[name] = sum_
print(f"{dict_}")