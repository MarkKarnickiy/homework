num = 1
my_list = (12, 4.67, True, None, (2 + 5j), {1, 2, 3}, [1,2,3], (1, 2, 3), "abs", {1:1, 2:2,3:3}, abs(2))
for i in my_list:
    print(f"{num} - {type(i)}" )
    num = num + 1