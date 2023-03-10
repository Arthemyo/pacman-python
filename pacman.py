import pygame
from pygame.draw import polygon

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
VELOCIDADE = 0.1

tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH)) 

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 10, 255)

olho_x = 0
olho_y = 0
raio_olho = 3

x = 20
y = 20
raio_pacman = 30
vel_x = VELOCIDADE
vel_y = VELOCIDADE
while True:
    # Roles
    x += vel_x
    y += vel_y

    olho_x = int(x) + 5
    olho_y = int(y) - 10

    if x > SCREEN_WIDTH - 30:
        vel_x = -VELOCIDADE
    if x < 30:
        vel_x = VELOCIDADE
    if y > SCREEN_HEIGTH - 30:
        vel_y = -VELOCIDADE
    if y < 30:
        vel_y = VELOCIDADE
    
    # Draw

    tela.fill(BLACK)

    r = pygame.Rect(x - 30, y - 30, 60, 60)

    pygame.draw.circle(tela, YELLOW, (int(x), int(y)), raio_pacman)
    pygame.draw.circle(tela, BLACK, (olho_x, olho_y), raio_olho)
    pygame.draw.polygon(tela, BLACK, [(int(x), int(y) + 10), (int(x) + raio_pacman, int(y) + 10), (int(x) + raio_pacman, int(y) - raio_pacman + 10)])

    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    
    pygame.display.update()
            