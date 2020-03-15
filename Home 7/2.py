class Clothes:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def square_c(self):
        return self.w / 6.5 + 0.5
    def square_j(self):
        return self.h * 2 + 0.3
    @property
    def square_full(self):
        return str(f'Общая площадь ткани: '
                   f' {(self.w / 6.5 + 0.5) + (self.h * 2 + 0.3)}')
class Coat(Clothes):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.coat_s = round(self.w / 6.5 + 0.5)
    def __str__(self):
        return f'Площадь ткани для пальто: {self.coat_s}'
class Jacket(Clothes):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.jacket_s = round(self.h * 2 + 0.3)
    def __str__(self):
        return f'Площадь ткани для костюма: {self.jacket_s}'
c = Coat(10, 40)
j = Jacket(30, 70)
print(c)
print(j)
print(j.square_c())
print(j.square_j())
print(c.square_full)
