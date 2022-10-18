import pygame
from random import randrange

RES, SIZE = 800, 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = (randrange(0, RES, SIZE), randrange(0, RES, SIZE))
if apple == (x, y):
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5
score = 0
background1 = pygame.image.load('bg1.jpg')
background2 = pygame.image.load('bg2.jpg')
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
variants = randrange(1, 3)

# Images
coin = pygame.image.load('coin.png')
snake_img = pygame.image.load('snake2.png')
icon = pygame.image.load('icon.png')

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Open sans', 35, bold=True)
font_end = pygame.font.SysFont('Open sans', 66, bold=True)
pygame.display.set_caption('Snake Game')
pygame.display.set_icon(icon)

while True:
    if score < 15:
        screen.blit(background1, (0, 0))
    else:
        screen.blit(background2, (0, 0))

    # Drawing snake and apple
    [screen.blit(snake_img, (i, j)) for i, j in snake]

    screen.blit(coin, apple)

    # Snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        for p in snake:
            if apple == p:
                apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        if len(snake) % 2 == 0:
            fps += 1

    # Show score
    render_score = font_score.render(f'SCORE: {score}', True, 'red', 'white')
    screen.blit(render_score, (5, 5))

    pygame.display.flip()
    clock.tick(fps)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if x < 0 or x >= RES or y < 0 or y >= RES or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, 'red', 'white')
            screen.blit(render_end, (RES // 2 - 160, RES // 2 - 100))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    # Control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}
