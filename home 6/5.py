class Stationary:
    title = "Тема"
    def draw(self):
        print("Отрисовка")

class Pen(Stationary):
    def draw(self):
        print("Я рисую ручкой")
class Pencil(Stationary):
    def draw(self):
        print("Я рисую карандашом")
class Handle(Stationary):
    def draw(self):
        print("Я рисую маркером ")
s = Stationary()
s.draw()
p = Pen()
p.draw()
p1 = Pencil()
p1.draw()
h = Handle()
h.draw()