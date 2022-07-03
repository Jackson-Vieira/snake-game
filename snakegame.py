import pygame
import random

from sys import exit
from time import time
from pygame.locals import *

pygame.init()

#Draw text
def draw_text(posx,posy, msg, screen, size=26):
    font = pygame.font.get_default_font()
    my_font = pygame.font.SysFont(font, size, 1, 0)

    font_render = my_font.render(msg, 1, (255,255,255))
    screen.blit(font_render, (posx,posy))

#Apple Position
def pos_maca(maca,x,y,snake_body):
    if x % 40 != 0: x += 40-(x%40)
        
    if y % 40 != 0: y += 40-(y%40)
        

    while (x,y) in snake_body:
        x, y = random.randint(0, 760), random.randint(0, 760)
        if x % 40 != 0: x += 40-(x%40)
        if y % 40 != 0: y += 40-(y%40)
    
    maca.x = x
    maca.y = y

def game():
    start_time = time()
    #MOVEMENT
    right = True
    left = top = bot = False

    #SETTINGS
    BK_COLOR = (0, 0, 0)
    COLOR_SNAKE = [(0, 255, 0), (50, 190, 50)]
    COLOR_MACA = (255, 0, 0)
    SCREEN_SIZE = (800, 800)

    #SCREEN
    screen = pygame.display.set_mode((SCREEN_SIZE))
    pygame.display.set_caption("SNAKE GAME")


    #SNAKE
    x_snake = 0
    y_snake = 0

    snake = pygame.Rect(x_snake, y_snake, 40, 40)


    snake_body = []
    max_body = 5

    #MAÇA
    maca = pygame.Rect(100, 100, 40, 40)
    points = 0

    clock = pygame.time.Clock()

    run = True
    while run:
        screen.fill(BK_COLOR)
        clock.tick(15) # FRAMES/SECOND

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_a and right == False:
                    left = True
                    right = top = bot = False
                if event.key == K_d and left == False:
                    right = True
                    bot = top = left = False
                if event.key == K_s and top == False:
                    bot = True
                    right = top = left = False
                if event.key == K_w and bot == False:
                    top = True
                    right = bot = left = False
                            
        if right:
            snake.x += 40
            left = False
        elif left:
            snake.x -= 40
        elif top:
            snake.y -= 40
        elif bot:
            snake.y += 40

        actual_pos_x = snake.x
        actual_pos_y = snake.y

        #EVENTS
        if actual_pos_x < 0:
            run = False
        elif actual_pos_x >= screen.get_width():
            run = False
        elif actual_pos_y < 0:
            run = False
        elif actual_pos_y >= screen.get_height():
            run = False
        elif (actual_pos_x, actual_pos_y) in snake_body:
            run = False

        else:
            #COLISIONS
            if snake.colliderect(maca):
                x_random = random.randint(0, 760)
                y_random = random.randint(0, 760)
                pos_maca(maca,x_random,y_random,snake_body)
                max_body += 1
                points += 1
            
            #DRAWS
            snake_body.append((actual_pos_x,actual_pos_y))
            if len(snake_body) >= max_body:
                snake_body.pop(0)

            for i, pos in enumerate(snake_body):
                pygame.draw.rect(screen, COLOR_SNAKE[i%2], (pos[0], pos[1], 40, 40))
            
            draw_text(680, 40,f'Points: {points}', screen)
            draw_text(600, 40, f"Size: {max_body}",screen)
            pygame.draw.rect(screen, COLOR_SNAKE[0], snake)
            pygame.draw.rect(screen, COLOR_MACA, maca)
            pygame.display.update()

    end_time = time()
    if snake_body == 400:
        print("Nice strategy!")
        
    else:
        print("Try again!")
    print("Elapsed Time: {:.2f}s".format(end_time-start_time))

if __name__ == '__main__':
    game()