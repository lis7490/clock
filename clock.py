from calendar import month
from datetime import datetime, time, timedelta
import time as time_module
import pygame


pygame.mixer.init()



notif = ""
while notif != "сигнал" and notif != "текст":
    try:
        notif = input("Введите тип оповещения: cигнал или текст: ")
        if notif != "сигнал" and notif != "текст":
            raise ValueError
    except ValueError:
        print("Ошибка! Пример ввода: cигнал")

if notif == "сигнал":
    def init_music():
        """Запрашивает у пользователя выбор мелодии для будильника"""
        music_list = ["mellen.mp3", "morning.mp3", "Barbarossa.mp3"]
        music = ''
        while music not in music_list:
            try:

                music = input(f"Выберите мелодию из списка: {music_list[0]}, {music_list[1]}, {music_list[2]}:  ")
                if music not in music_list:
                    raise ValueError

            except ValueError:
                print(f"Ошибка. Введите мелодию из списка: {music_list[0]}, {music_list[1]} (например: mellen.mp3).")
        sound = pygame.mixer.Sound(music)

        return sound

    choice_music = init_music()  # функция выбора музыки

def notification():
    """Запрашивает у пользователя тип уведомления: звук или текстовое сообщение"""

    if notif == "текст":
        print(f"\nЗвонит БУДИЛЬНИК! Дзынь Дзынь! Просыпайся, лодырь, пора пахать!")
    else:

        while True:
            choice_music.play(loops=-1)                     # loops=-1 - Зацикливание музыки
            command = ""

            while command != "звук":
                command = input(f"\nВведите 'звук' для остановки будильника: ").strip().lower()
                if command == "звук":
                    pygame.mixer.stop()  # Останавливаем все звуки
                    print("Звук отключен!")
            repeat = ''
            while repeat != "да" and repeat != "нет":
                try:
                    repeat = input("Хотите повторить сигнал через 5 минут? да/нет: ")
                    if repeat != "да" and repeat != "нет":
                        raise ValueError
                except ValueError:
                    print("Ошибка! Введите: да/нет")
            if repeat == "нет":
                break


            time_module.sleep(300)


choose_type_clock = input("Выберите тип будильника: одноразовый, ежедневный, по дням недели: ")
if choose_type_clock == "одноразовый":
    month = []
    date = []
    hrs = []
    mnt = []
    dict = ""

    while dict != "нет":
        user_input = input("Введите время в формате Месяц:Число:Часы:Минуты : ")
        a, b, c, d = user_input.split(':')
        month.append(a)
        date.append(b)
        hrs.append(c)
        mnt.append(d)
        dict = input("Вы хотите добавить будильник? да/нет: ")

        while True:
            current_time = datetime.now().strftime('%m,%d %H:%M:%S')  # Текущее время
            print(f"\rТекущее время: {current_time}", end="", flush=True)
            A = 0
            B = 0
            C = 0
            D = 0
            for k in hrs:
                if datetime.now().strftime('%m') == k:
                    C = 1
            for l in mnt:
                if datetime.now().strftime('%d') == l:
                    D = 1
            for i in hrs:
                if datetime.now().strftime('%H') == i:
                    A = 1
            for j in mnt:
                if datetime.now().strftime('%M') == j:
                    B = 1
            if A == 1 and B == 1 and C == 1 and D == 1:
                notification()

                time_module.sleep(60)
            time_module.sleep(1)





elif choose_type_clock == "ежедневный":
    hrs = []  # Список часов
    mnt = []  # Список минут
    dict = ""

    while dict != "нет":
        user_input = input("Введите время в формате Часы:Минуты : ")
        c, d = map(int, user_input.split(':'))
        hrs.append(c)
        mnt.append(d)
        dict = input("Вы хотите добавить будильник? да/нет: ")

        while True:
            current_time = datetime.now().time()  # Текущее время
            print(f"\rТекущее время: {current_time.strftime('%H:%M:%S')}", end="", flush=True)
            A = 0
            B = 0
            for i in hrs:
                if current_time.hour == i:
                    A = 1
            for j in mnt:
                if current_time.minute == j:
                    B = 1
            if A == 1 and B == 1:
                notification()

                time_module.sleep(60)
            time_module.sleep(1)


else:
    print(choose_type_clock)




# def get_user_time():
#     """Запрашивает у пользователя время в формате Часы:Минуты и возвращает time"""
#     while True:
#         user_input = input("Введите время в формате Часы:Минуты : ")
#         try:
#             hours, minutes = map(int, user_input.split(':'))
#             if 0 <= hours < 24 and 0 <= minutes < 60:
#                 return time(hour=hours, minute=minutes)
#             else:
#                 print("Ошибка: часы (0-23) или минуты (0-59) вне диапазона.")
#         except ValueError:
#             print("Ошибка: используйте формат Часы:Mинуты (например, 14:30).")

# user_time = get_user_time()





