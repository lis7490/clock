
from datetime import datetime, time, timedelta
import time as time_module
import pygame

current_time = datetime.now().strftime('%m,%d %H:%M:%S')
user_input = input("Введите время в формате Месяц:Число:Часы:Минуты : ")
a, b, c, d = user_input.split(':')

if datetime.now().strftime('%m') == a:
    print("да")

print(current_time)
