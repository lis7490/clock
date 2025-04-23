from datetime import datetime, time, timedelta
import time as time_module

a = []
b = []
dict = ""

while dict != "нет":
    user_input = input("Введите время в формате Часы:Минуты : ")
    c, d = map(int, user_input.split(':'))
    a.append(c)
    b.append(d)
    dict = input("Да или Нет: ")

while True:
    current_time = datetime.now().time()  # Текущее время
    print(f"\rТекущее время: {current_time.strftime('%H:%M:%S')}", end="", flush=True)

    for i in a:
        if current_time.hour == i:
            d = 1
    for j in b:
        if current_time.minute == j:
            c = 1
    if d == 1 and c == 1:
        print("ДААААА")
    time_module.sleep(1)







print(a, b)
