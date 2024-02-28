import pygame
from pygame import *
import sys
pygame.init()

# COLORS
white = [255,255, 255]
red = [255,0,0]
black = [0,0,0]

game_width = 900
game_height = 600

game_window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Snake-Game")
pygame.display.update()

# GAME SPECIFIC VARIABLES
exit_game = False
game_over = False
fps=32
snake_x = 45
snake_y = 55
snake_size = 10
velocity_x = 15
velocity_y = 10

clock = pygame.time.Clock()

# GAME LOOP
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x +5


    
    game_window.fill(white)
    pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

