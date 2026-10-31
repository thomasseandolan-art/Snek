import pygame
import random

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Welcome to my game!")

player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
player = pygame.image.load("imgs/tile_0098.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player_x = 350
player_y = 540
player_vel_x = 0
player_vel_y = 0
falling_object = pygame.image.load("imgs/tile_0151.png").convert_alpha()
falling_object = pygame.transform.scale(falling_object, (50, 50))

falling_object_x = 300
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3
def collision_detection():
    return (player_x <= (falling_object_x + int(falling_object.get_width())) and
    (player_x + player.get_width()) >= falling_object_x and
    player_y <= (falling_object_y + falling_object.get_height() +5) and
    (player_y + player.get_height()) >= falling_object_y)

game_state = 1

grass = pygame.image.load("imgs/tile_0001.png").convert_alpha()
grass = pygame.transform.scale(grass, (50, 50))

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 quit(0)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.3
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.3
            if event.key == pygame.K_UP:
                player_vel_y = -0.3
            if event.key == pygame.K_DOWN:
                player_vel_y = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_vel_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_vel_y = 0
    if collision_detection():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.get_width() - 50)
    falling_object_x += falling_object_vel_x
    falling_object_y += falling_object_vel_y


    #output
    window.fill((0, 0,0))
    for y in range(0, 600, 50):
        for x in range(0, 800, 50):
            window.blit(grass, (x, y))
    player_x += player_vel_x
    player_y += player_vel_y
    if player_x < 0:
        player_x = 0
    if player_x > window.get_width() - player.get_width():
        player_x = window.get_width() - player.get_width()

    if player_y < 0:
        player_y = 0
    if player_y > window.get_height() - player.get_height():
        player_y = window.get_height() - player.get_height()

    if falling_object_y >= 600:
        game_state = 2
    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))
    pygame.display.flip()


