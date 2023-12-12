import pygame
import sudokum
import requests

#definir janela
width = 550
height = 550
bg_color = (0, 247, 245)
grid_element_color = (52, 31, 151)
bg_color_dif1 = (0,200,255)
bg_color_dif2 = (0,200,255)
bg_color_dif3 = (0,200,255)
bg_color_dif4 = (0,200,255)
bg_color_dif5 = (0,200,255)
bg_color_dif6 = (0,200,255)
bg_color_dif7 = (0,200,255)
bg_color_dif8 = (0,200,255)
bg_color_dif9 = (0,200,255)

dificuldade = 1 # assim começa com a grelha vazia. Foi sem querer mas calhou bem
def main():
    global dificuldade, bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(bg_color)
    font = pygame.font.SysFont('Comic Sans MS', 35)
    retangulo_novo = pygame.Rect(50,0,100,50)
    pygame.draw.rect(win, (0,0,250), retangulo_novo)
    botao_novo = font.render('novo', True, (255,255,255))
    win.blit(botao_novo, (50,0))

    texto_dificuldade = font.render('dificuldade', True, (255, 255, 255))
    win.blit(texto_dificuldade, (0, 500))

    rect_dif_1 = pygame.Rect(200, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif1, rect_dif_1)
    texto_dif_1 = font.render('1', True, (0,0,0))
    win.blit(texto_dif_1, (200, 500))

    rect_dif_2 = pygame.Rect(230, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif2, rect_dif_2)
    texto_dif_2 = font.render('2', True, (0,0,0))
    win.blit(texto_dif_2, (230, 500))

    rect_dif_3 = pygame.Rect(260, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif3, rect_dif_3)
    texto_dif_3 = font.render('3', True, (0,0,0))
    win.blit(texto_dif_3, (260, 500))
    
    rect_dif_4 = pygame.Rect(290, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif4, rect_dif_4)
    texto_dif_4 = font.render('4', True, (0,0,0))
    win.blit(texto_dif_4, (290, 500))

    rect_dif_5 = pygame.Rect(320, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif5, rect_dif_5)
    texto_dif_5 = font.render('5', True, (0,0,0))
    win.blit(texto_dif_5, (320, 500))

    rect_dif_6 = pygame.Rect(350, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif6, rect_dif_6)
    texto_dif_6 = font.render('6', True, (0,0,0))
    win.blit(texto_dif_6, (350, 500))

    rect_dif_7 = pygame.Rect(380, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif7, rect_dif_7)
    texto_dif_7 = font.render('7', True, (0,0,0))
    win.blit(texto_dif_7, (380, 500))

    rect_dif_8 = pygame.Rect(410, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif8, rect_dif_8)
    texto_dif_8 = font.render('8', True, (0,0,0))
    win.blit(texto_dif_8, (410, 500))

    rect_dif_9 = pygame.Rect(440, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif9, rect_dif_9)
    texto_dif_9 = font.render('9', True, (0,0,0))
    win.blit(texto_dif_9, (440, 500))


    for i in range(0,10):
        if (i % 3 == 0):
            grossura_linha = 4
        else:
            grossura_linha = 2
        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), grossura_linha) #desenhar linhas verticais da grelha
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), grossura_linha) #desenhar linhas horizonrais da grelha
    pygame.display.update() #sem esta linha não aparece nada na janela. Fica tudo preto
    
    grid = sudokum.generate(mask_rate=(dificuldade)) #definir nova grid(após clicar em 'novo')
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

                #definir os botões da dificuldade
                if  rect_dif_1[0] <= mouse[0] <= rect_dif_1[0] + rect_dif_1[2] and rect_dif_1[1] <= mouse[1] <= rect_dif_1[1] + rect_dif_1[3]:
                    dificuldade = 0.1
                    bg_color_dif1 = (0,100,255)
                    bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_2[0] <= mouse[0] <= rect_dif_2[0] + rect_dif_2[2] and rect_dif_2[1] <= mouse[1] <= rect_dif_2[1] + rect_dif_2[3]:
                    dificuldade = 0.2
                    bg_color_dif2 = (0,100,255)
                    bg_color_dif1, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_3[0] <= mouse[0] <= rect_dif_3[0] + rect_dif_3[2] and rect_dif_3[1] <= mouse[1] <= rect_dif_3[1] + rect_dif_3[3]:
                    dificuldade = 0.3
                    bg_color_dif3 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_4[0] <= mouse[0] <= rect_dif_4[0] + rect_dif_4[2] and rect_dif_4[1] <= mouse[1] <= rect_dif_4[1] + rect_dif_4[3]:
                    dificuldade = 0.4
                    bg_color_dif4 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_5[0] <= mouse[0] <= rect_dif_5[0] + rect_dif_5[2] and rect_dif_5[1] <= mouse[1] <= rect_dif_5[1] + rect_dif_5[3]:
                    dificuldade = 0.5
                    bg_color_dif5 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_6[0] <= mouse[0] <= rect_dif_6[0] + rect_dif_6[2] and rect_dif_6[1] <= mouse[1] <= rect_dif_6[1] + rect_dif_6[3]:
                    dificuldade = 0.6
                    bg_color_dif6 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_7[0] <= mouse[0] <= rect_dif_7[0] + rect_dif_7[2] and rect_dif_7[1] <= mouse[1] <= rect_dif_7[1] + rect_dif_7[3]:
                    dificuldade = 0.7
                    bg_color_dif7 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif8, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_8[0] <= mouse[0] <= rect_dif_8[0] + rect_dif_8[2] and rect_dif_8[1] <= mouse[1] <= rect_dif_8[1] + rect_dif_8[3]:
                    dificuldade = 0.8
                    bg_color_dif8 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif9 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
                if  rect_dif_9[0] <= mouse[0] <= rect_dif_9[0] + rect_dif_9[2] and rect_dif_9[1] <= mouse[1] <= rect_dif_9[1] + rect_dif_9[3]:
                    dificuldade = 0.9
                    bg_color_dif9 = (0,100,255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8 = (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255), (0,200,255)
                 
                    print(dificuldade)
            
main()