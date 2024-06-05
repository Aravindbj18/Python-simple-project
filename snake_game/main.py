import pygame
import sys
from snake import Snake
from food import Food

BLACK =(0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
FPS = 10
board_size = 400
cell_size = 10
speed = 10
pygame.init()
screen = pygame.display.set_mode((board_size, board_size))
clock = pygame.time.Clock()

snake = Snake(board_size/2 , board_size/2, board_size, cell_size, speed=speed, direction= 'RIGHT')
food = Food(board_size, cell_size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != 'RIGHT': 
                snake.direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake.direction != 'LEFT': 
                snake.direction = 'RIGHT'  
            if event.key == pygame.K_UP and snake.direction != 'DOWN': 
                snake.direction = 'UP'
            if event.key == pygame.K_DOWN and snake.direction != 'UP': 
                snake.direction = 'DOWN'   
       
     
   

    screen.fill(BLACK)
    snake.update_position()
    pygame.draw.rect(screen,WHITE, (snake.x,snake.y , cell_size, cell_size))  
    pygame.draw.rect(screen, RED,(food.x, food.y, cell_size, cell_size))
    if snake.ate_food(food):
        food.spawn()
        snake.grow()

    
    print(snake.x, snake.y, food.x, food.y)
    pygame.display.flip()   
    clock.tick(FPS)   


   
        
       












             

