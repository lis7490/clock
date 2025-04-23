from datetime import datetime, time, timedelta
import time as time_module

a = []
b = []
dict = ""
e = 0
f = 0
while dict != "нет":
    user_input = input("Введите время в формате Часы:Минуты : ")
    c, d = map(int, user_input.split(':'))
    a.append(c)
    b.append(d)
    dict = input("Да или Нет: ")

while True:
    current_time = datetime.now().time()  # Текущее время
    print(f"\rТекущее время: {current_time.strftime('%H:%M:%S')}", end="", flush=True)
    e = 0
    f = 0
    for i in a:
        if current_time.hour == i:
            e = 1
    for j in b:
        if current_time.minute == j:
            f = 1
    if e == 1 and f == 1:
        print(f"\nЗвонит БУДИЛЬНИК! Дзынь Дзынь! Просыпайся, лодырь, пора пахать!)")
        time_module.sleep(60)
    time_module.sleep(1)







print(a, b)
