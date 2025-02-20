import pygame
import requests
import os
import sys

API_KEY = '80b44bb1-d0c2-4df3-b6da-8de07ce8c027'

l1 = 37.620393
l2 = 55.753930
z = 10


def load(url):
    response = requests.get(url)
    if not response:
        print("Ошибка загрузки карты")
        sys.exit(1)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def main():
    map_file = load(f"https://static-maps.yandex.ru/1.x/?ll={l1},{l2}&z={z}&l=map&size=600,450&apikey={API_KEY}")
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    pygame.display.set_caption("Карта")

    map_image = pygame.image.load(map_file)
    screen.blit(map_image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()
