import pygame
import sudokum
import requests

#definir janela
width = 550
height = 550
bg_color = (0, 247, 245)
grid_element_color = (52, 31, 151)

def main():
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(bg_color)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    retangulo_novo = pygame.Rect(50,0,100,50)
    pygame.draw.rect(win, (0,0,250), retangulo_novo)
    botao_novo = font.render('novo', True, (255,255,255))
    win.blit(botao_novo, (50,0))
    
    for i in range(0,10):
        if (i % 3 == 0):
            grossura_linha = 4
        else:
            grossura_linha = 2
        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), grossura_linha) #desenhar linhas verticais da grelha
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), grossura_linha) #desenhar linhas horizonrais da grelha
    pygame.display.update() #sem esta linha não aparece nada na janela. Fica tudo preto
    
    grid = sudokum.generate(mask_rate=(0.1)) #definir nova grid(após clicar em 'novo')
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = font.render(str(grid[i][j]), True, grid_element_color)
                win.blit(value, ((j+1)*50+15, (i+1)*50))
    pygame.display.update()

    while True:
        mouse = pygame.mouse.get_pos() #tem de ficar aqui dentro do while, senao fica sempre com as mesmas coordenadas
        #print(mouse) #imprime as coordenadas da posição do rato no formato (x, y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (retangulo_novo[0] <= mouse[0] <= retangulo_novo[0]+retangulo_novo[2]) and (retangulo_novo[1] <= mouse[1] <= retangulo_novo[1]+retangulo_novo[3]):
                    # novo_sudoku()
                    main() #vai ao main e cria uma nova grid com novos numeros
                
main()