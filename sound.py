from random import choice

import pygame
from pygame.examples.music_drop_fade import music_file_list

pygame.mixer.init()
def init_music():
    music = input("Выберите мелодию из списка: mellen.mp3, morning.mp3: ")
    sound = pygame.mixer.Sound(music)
    return sound

choice_music = init_music()


for i in range(5):
    print(f"Итерация {i}")
    if i == 3:
        choice_music.play()
        while True:
            try:
                command = input("Введите 'стоп' для остановки звука: ").strip().lower()
                if command != "стоп":
                    raise ValueError

                if command == "стоп":
                    pygame.mixer.stop()  # Останавливаем все звуки
                    print("Звук остановлен!")
            except ValueError:
                print("Введенная команда не верна, нужно вводить: 'стоп'")
                break


        #pygame.time.delay(100000)  # Задержка (мс)