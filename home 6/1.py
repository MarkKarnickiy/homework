class TrafficLight:
    _color = "Цвет"
    def running(self):
        _color = "Красный"
        time = 1
        while time != 8:
            print(f"{_color},{time}")
            time = time + 1
            if time == 8:
                break
        _color = "Желтый"
        time = 1
        while time != 3:
            print(f"{_color},{time}")
            time = time + 1
            if time == 3:
                break
        _color = "Зеленый"
        time = 1
        while time != 10:
            print(f"{_color},{time}")
            time = time + 1
            if time == 10:
                break


t = TrafficLight()
t.running()

