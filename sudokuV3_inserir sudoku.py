import pygame
import sudokum
import requests

#definir janela
width = 550
height = 550
bg_color = (0, 247, 245)
grid_element_color = (52, 31, 151)
#definir o sudoku a ser resolvido
grid = sudokum.generate(mask_rate=(0.1)) 
print(grid)
print(grid[0][1])
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
    
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = font.render(str(grid[i][j]), True, grid_element_color)
                win.blit(value, ((j+1)*50+15, (i+1)*50))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()