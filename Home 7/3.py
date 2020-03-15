class Cell:
    def __init__(self, quan):
        self.quan = int(quan)
    def __str__(self):
        return f'Клеточки:  {self.quan * "#"}'
    def __add__(self, other):
        return Cell(self.quan + other.quan)
    def __sub__(self, other):
        return self.quan - other.quan if (self.quan - other.quan) > 0 else print('- Клеточек не бывает!')
    def __mul__(self, other):
        return Cell(int(self.quan * other.quan))
    def __truediv__(self, other):
        return Cell(round(self.quan // other.quan))
    def make_order(self, cells):
        r = ""
        for i in range(int(self.quan / cells)):
            r += f'{"#" * cells} \\n'
        r += f'{"#" * (self.quan % cells)}'
        return r
c1 = Cell(100)
c2 = Cell(50)
print(c1)
print(c1 + c2)
print(c2 - c1)
print(c2.make_order(5))
print(c1.make_order(10))
print(c1 / c2)
