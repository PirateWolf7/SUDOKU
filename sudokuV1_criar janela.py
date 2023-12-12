import pygame
import sudokum
import requests

#definir janela
width = 550
height = 550
bg_color = (0, 247, 245)

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(bg_color)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    pygame.display.update() #sem esta linha não aparece nada na janela. Fica tudo preto
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()