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
    for i in range(0,10):
        if (i % 3 == 0):
            grossura_linha = 4
        else:
            grossura_linha = 2
        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), grossura_linha) #desenhar linhas verticais da grelha
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), grossura_linha) #desenhar linhas horizonrais da grelha
    pygame.display.update() #sem esta linha não aparece nada na janela. Fica tudo preto
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()