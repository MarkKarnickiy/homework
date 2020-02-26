a = float(input("Ведите число: "))
b = float(input("Ведите число: "))
c = float(input("Ведите число: "))
def my_func():
    my_list = [a,b,c]
    max_sum = float(a + b + c - min(my_list))
    return max_sum
sum = my_func()
print(my_func())
