import pygame
import requests
import os
import sys


API_KEY = '80b44bb1-d0c2-4df3-b6da-8de07ce8c027'

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
    l1 = 37.620393
    l2 = 55.753930
    z = 10
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    pygame.display.set_caption("Карта")

    map_file = load(f"https://static-maps.yandex.ru/1.x/?ll={l1},{l2}&z={z}&l=map&size=600,450&apikey={API_KEY}")
    map_image = pygame.image.load(map_file)
    screen.blit(map_image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                step = 360 / (2 ** (z + 1))

                if event.key == pygame.K_UP:
                    l2 += step
                elif event.key == pygame.K_DOWN:
                    l2 -= step
                elif event.key == pygame.K_RIGHT:
                    l1 += step
                elif event.key == pygame.K_LEFT:
                    l1 -= step

                l2 = max(-90, min(l2, 90))
                l1 = max(-180, min(l1, 180))

                map_file = load(f"https://static-maps.yandex.ru/1.x/?ll={l1},{l2}&z={z}&l=map&size=600,450&apikey={API_KEY}")
                map_image = pygame.image.load(map_file)
                screen.blit(map_image, (0, 0))
                pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()
