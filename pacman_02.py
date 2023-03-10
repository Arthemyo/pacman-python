from typing import Sized
import pygame
from pygame.constants import K_RIGHT, K_UP

pygame.init()

WIDTH_SCREEN = 800
HEIGTH_SCREEN = 600

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGTH_SCREEN))
anima_boca = 0
fonte = pygame.font.SysFont("arial", 24, True, False)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
SPEED = 1



class Cenario:
    def __init__(self, tamanho, pac):
        self.tamanho = tamanho
        self.pontos = 0
        self.pacman = pac
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half_tamanho = self.tamanho // 2
            cor = BLACK
            if coluna == 2:
                cor = BLUE
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho))
            if coluna == 1:
                pygame.draw.circle(tela, YELLOW, (x + half_tamanho, y + half_tamanho), self.tamanho // 10)

    def print_cenario(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)
    
    def pintar_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        text = fonte.render("Score: {}".format(self.pontos), True, YELLOW)
        tela.blit(text, (pontos_x, 50))

    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao

        if 0 <= col < 28 and 0 <= lin < 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.matriz[lin][col] = 0

class Pacman:
    def __init__(self, size):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = size
        self.raio_pacman = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.anima_boca = 0

    def pint(self, tela, anima_boca):
        # Draw body from the pacman
        pygame.draw.circle(tela, YELLOW, (self.centro_x, self.centro_y), self.raio_pacman)

        # Draw mounth from the pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_inferior = (self.centro_x + self.raio_pacman, self.centro_y)
        labio_superior = (self.centro_x + self.raio_pacman + self.anima_boca, self.centro_y - self.raio_pacman)
        print(labio_superior)
        boca = [canto_boca, labio_inferior, labio_superior]

        pygame.draw.polygon(tela, BLACK, boca)

        # Draw eye from the pacman
        olho_x = int(self.centro_x + self.raio_pacman / 3)
        olho_y = int(self.centro_y - self.raio_pacman * 0.70)
        olho_raio = int(self.raio_pacman / 10)

        pygame.draw.circle(tela, BLACK, (olho_x, olho_y), olho_raio)

    def calcular_regra(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio_pacman)
        self.centro_y = int(self.linha * self.tamanho + self.raio_pacman)

    def processar_eventos(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    pacman.vel_x += SPEED
                if e.key == pygame.K_LEFT:
                    pacman.vel_x -= SPEED
                if e.key == pygame.K_DOWN:
                    pacman.vel_y += SPEED
                if e.key == pygame.K_UP:
                    pacman.vel_y -= SPEED
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    pacman.vel_x = 0
                if e.key == pygame.K_LEFT:
                    pacman.vel_x = 0
                if e.key == pygame.K_DOWN:
                    pacman.vel_y = 0
                if e.key == pygame.K_UP:
                    pacman.vel_y = 0
               
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

if __name__  == "__main__":

    size = 630 // 30
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)
    

    while True:
        # Calculo da regra
        pacman.calcular_regra()
        cenario.calcular_regras()

        # Print in screen
        screen.fill(BLACK)
        cenario.print_cenario(screen)
        pacman.pint(screen, anima_boca)

        # Captura de evento
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(events)
                
            
        pygame.display.update()
        pygame.time.delay(100)