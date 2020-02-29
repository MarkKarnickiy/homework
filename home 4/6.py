from itertools import count, cycle
num = int(input("Enter start number: "))
fnum = int(input("Enter final number: "))
for i in count(num):
    if i > fnum:
        break
    else:
        print(i)
text = input("Enter text: ").split()
copy = int(input('Enter the number of copies: '))
c = 0
for i in cycle(text):
    if c >= copy:
        break
    else:
        print(i)
        c = c + 1