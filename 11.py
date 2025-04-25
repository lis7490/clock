from datetime import datetime, time, timedelta
import time as time_module

def get_user_time():
    """Запрашивает у пользователя время в формате Часы:Минуты и возвращает time"""
    while True:
        user_input = input("Введите время в формате Часы:Минуты : ")
        try:
            hours, minutes = map(int, user_input.split(':'))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return time(hour=hours, minute=minutes)
            else:
                print("Ошибка: часы (0-23) или минуты (0-59) вне диапазона.")
        except ValueError:
            print("Ошибка: используйте формат Часы:Mинуты (например, 14:30).")

user_time = get_user_time()

def main():

    print(f"Будильник сработает в: {user_time.strftime('%H:%M')}")

    while True:
        current_time = datetime.now().time()  # Текущее время
        print(f"\rТекущее время: {current_time.strftime('%H:%M:%S')}", end="", flush=True)

        if current_time.hour == user_time.hour and current_time.minute == user_time.minute:
            print(f"\rДА")
            time_module.sleep(60)             #для задержки цикла, пока не пройдёт минута после отмены звука или текста


        time_module.sleep(1)  # Пауза 1 секунда между циклами

main()