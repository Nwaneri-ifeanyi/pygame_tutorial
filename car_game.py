import pygame
from pygame.locals import *
import random

size = width, height = (800, 700)
road_w = int(width / 1.6)
road_mark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode(size)
# set tittle
pygame.display.set_caption("my car game")
# set background colour
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()

# load images
# load player vehicle
car = pygame.image.load('car2.png')
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.9

# load enemy vehicle
car2 = pygame.image.load('car1.png')
car2_loc = car.get_rect()
car2_loc.center = left_lane, height * 0.1

counter = 0
# game loop
while running:
    counter += speed
    if counter == 1024:
        speed += 0.25
        counter = 0
        print('level up', speed)
    # animate enemy vehicle
    car2_loc[1] += 1
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, - 200
        else:
            car2_loc.center = left_lane, -200

    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 50:
        print("GAME OVER! YOU LOST")
        break
    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])

    # draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height)
    )

    pygame.draw.rect(screen,
                     (255, 240, 60),
                     (width / 2 - road_mark_w / 2, 0, road_mark_w, height))

    pygame.draw.rect(screen,
                     (255, 255, 255),
                     (width / 2 - road_w / 2 + road_mark_w * 3, 0, road_mark_w, height))

    pygame.draw.rect(screen,
                     (255, 255, 255),
                     (width / 2 + road_w / 2 - road_mark_w * 3, 0, road_mark_w, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()
