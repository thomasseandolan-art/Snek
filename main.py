import pygame
import random
from pathlib import Path

pygame.init()

window = pygame.display.set_mode((800, 660))
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
lives = 3
score = 0
high_score_path = Path(__file__).with_name("high_score.txt")

try:
    with open(high_score_path, "r") as file:
        high_score = int(file.read())
except (FileNotFoundError, ValueError):
    high_score = 0

grass = pygame.image.load("imgs/tile_0001.png").convert_alpha()
grass = pygame.transform.scale(grass, (50, 50))

heart_full = pygame.image.load("imgs/tile_0044.png").convert_alpha()
heart_full = pygame.transform.scale(heart_full, (32, 32))
heart_empty = pygame.image.load("imgs/tile_0046.png").convert_alpha()
heart_empty = pygame.transform.scale(heart_empty, (32, 32))

title_font = pygame.font.Font(None, 60)
ui_font = pygame.font.Font(None, 32)
restart_button = pygame.Rect(290, 335, 220, 60)
coin_image = falling_object
bomb_image = pygame.image.load("imgs/1.png").convert_alpha()
bomb_image = pygame.transform.scale(bomb_image, (100, 100))

def new_drop():
    bomb = random.random() < 0.2
    if bomb:
        image = bomb_image
    else:
        image = coin_image
    x = random.randint(0, window.get_width() - image.get_width())
    return image, bomb, x, 0

falling_object, is_bomb, falling_object_x, falling_object_y = new_drop()
while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                 quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and game_state == 2:
                if restart_button.collidepoint(event.pos):
                    lives = 3
                    score = 0
                    player_x = 350
                    player_y = 540
                    player_vel_x = 0
                    player_vel_y = 0
                    falling_object, is_bomb, falling_object_x, falling_object_y = new_drop()
                    game_state = 1


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
    if game_state == 1:
        falling_object_x += falling_object_vel_x
        falling_object_y += falling_object_vel_y

        if collision_detection():
            if is_bomb:
                lives -= 1
            else:
                score += 1
                if score > high_score:
                    high_score = score
                    with open(high_score_path, "w") as file:
                        file.write(str(high_score))

            falling_object, is_bomb, falling_object_x, falling_object_y = new_drop()

        elif falling_object_y >= 600:
            if not is_bomb:
                lives -= 1

            falling_object, is_bomb, falling_object_x, falling_object_y = new_drop()

        if lives <= 0:
            game_state = 2
            player_vel_x = 0
            player_vel_y = 0


    #output
    window.fill((0, 0,0))
    for y in range(0, 600, 50):
        for x in range(0, 800, 50):
            window.blit(grass, (x, y))
    if game_state == 1:
        player_x += player_vel_x
        player_y += player_vel_y
    if player_x < 0:
        player_x = 0
    if player_x > window.get_width() - player.get_width():
        player_x = window.get_width() - player.get_width()

    if player_y < 0:
        player_y = 0
    if player_y > 600 - player.get_height():
        player_y = 600 - player.get_height()

    window.blit(player, (player_x, player_y))
    window.blit(falling_object, (falling_object_x, falling_object_y))
    for i in range(3):
        if i < lives:
            window.blit(heart_full, (20 + i * 40, 20))
        else:
            window.blit(heart_empty, (20 + i * 40, 20))
    pygame.draw.rect(window, (30, 35, 45), (0, 600, 800, 60))
    score_text = ui_font.render(f"Score: {score}", True, (255, 255, 255))
    best_text = ui_font.render(f"High score: {high_score}", True, (255, 255, 255))
    window.blit(score_text, (20, 620))
    window.blit(best_text, (440, 620))
    if game_state == 2:
        title = title_font.render("Game Over!", True, (255, 255, 255))
        message = ui_font.render("You ran out of lives", True, (255, 255, 255))
        window.blit(title, title.get_rect(center=(400, 225)))
        window.blit(message, message.get_rect(center=(400, 285)))

        pygame.draw.rect(window, (65, 150, 85), restart_button)
        label = ui_font.render("Play Again", True, (255, 255, 255))
        window.blit(label, label.get_rect(center=restart_button.center))

    pygame.display.flip()


