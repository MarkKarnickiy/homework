class Car:
    speed = 0
    color = "Color"
    name = "Name"
    is_police = "bool"
    turn = "right, left"
    def car_go(self,name,color,speed,is_police):
        if is_police == True:
            print(f"Полицейская машина {name} Цвета {color} выехала со скоростью {speed} км/ч")
        else:
            print(f"Машина {name} Цвета {color} выехала со скоростью {speed} км/ч")
    def car_stop(self,name,color,is_police):
        if is_police == True:
            print(f"Полицейская машина {name} Цвета {color} остановилась")
        else:
            print(f"Машина {name} Цвета {color} остановилась")
    def car_turn(self,name,color,is_police,turn):
        if is_police == True:
            print(f"Полицейская машина {name} Цвета {color} повернула в {turn}")
        else:
            print(f"Машина {name} Цвета {color} повернула в {turn}")
    def show_speed(self,speed):
        if speed > 60:
            print("Все впорядке. Ей можно.")
class Town_car(Car):
    def show_speed(self,speed):
        if speed > 60:
            print("Скорость превышена! Ограничение 60 км/ч")
class Work_car(Car):
    def show_speed(self,speed):
        if speed > 40:
            print("Скорость превышена! Ограничение 40 км/ч")
class Sport_car(Car):
    pass
class Police_car(Car):
    is_police = True
c = Car()
t = Town_car()
w = Work_car()
s = Sport_car()
p = Police_car()
t.car_go("reno","red",70,False)
t.car_stop("reno","red",False)
t.car_turn("reno","red",True,"left")
t.show_speed(70)


