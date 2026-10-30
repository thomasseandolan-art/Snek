import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Welcome to my game!")

player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
player = pygame.image.load("imgs/tile_0098.png").convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0
falling_object = pygame.surface.Surface((50, 50))
falling_object.fill((255, 255, 255))

falling_object_x = 300
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 quit(0)


        if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             player_vel_x = -0.2
         if event.key == pygame.K_RIGHT:
            player_vel_x = 0.2
        else:
            player_vel_x = 0
            player_vel_y = 0


    #output
    window.fill((0, 0,0))
    player_x += player_vel_x
    player_y += player_vel_y
    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))
    pygame.display.flip()


