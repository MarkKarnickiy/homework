in_sec = int(input("Введите время в секундах: "))
sec = in_sec % 3600 % 60
min =  in_sec % 3600 // 60
hour = in_sec // 3600
#day = 0
if min < 10:
    min = "0" + str(min)
if sec < 10:
    sec = "0" + str(sec)
while hour >= 24:
    hour = hour - 24
    #day = day + 1
if hour < 10:
    hour = "0" + str(hour)

print(f"Время: {hour}: {min}: {sec} ")
#print("День: " + str(day))

