from math import factorial
def fibo_gen(h):
    for i in h:
        yield factorial(i)
for i in fibo_gen(range(1,16)):
    print(i)