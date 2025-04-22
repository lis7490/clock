
def notification():
    if notif == "текст":
        print(f"\nВведённое время совпало с текущим! ({user_time.strftime('%H:%M')})")
    else:
        choice_music.play()
        while True:
            command = input(f"\nВведите 'звук' для остановки будильника: ").strip().lower()
            if command == "звук":
                pygame.mixer.stop()  # Останавливаем все звуки
                print("Звук отключен!")
notification()
