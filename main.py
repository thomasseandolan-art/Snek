import pygame

pygame.init()

window = pygame.display.set.mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set.caption("Welcome to my game!")

while True:
    #take input
    player_x = 0
    player_y = 0
    player_vel_x = 0
    player_vel_y = 0
    #output
    window.fill((255, 255, 255))
    window.blit(player) dest: (player_x, player_y)

    pygame.display.flip()
    while True:
        #take input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)

player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))

