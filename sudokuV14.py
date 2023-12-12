import pygame
import sudokum


# definir variáveis
width = 550
height = 550
bg_color = (0, 247, 245)
grid_element_color = (52, 31, 151)
bg_color_dif1 = (0, 200, 255)
bg_color_dif2 = (0, 200, 255)
bg_color_dif3 = (0, 200, 255)
bg_color_dif4 = (0, 200, 255)
bg_color_dif5 = (0, 200, 255)
bg_color_dif6 = (0, 200, 255)
bg_color_dif7 = (0, 200, 255)
bg_color_dif8 = (0, 200, 255)
bg_color_dif9 = (0, 200, 255)
dificuldade = 1  # assim começa com a grelha vazia
solucao = 0
buffer = 5


def insert(win, position):  # FUNÇÃO PARA INSERIR NUMEROS MANUALMENTE

    i, j = position[1], position[0]
    font = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i-1][j-1] != 0):
                    return
                if (event.key == 48):
                    grid_alterada[i-1][j-1] = event.key - 48
                    pygame.draw.rect(
                        win, bg_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    pygame.display.update()
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(
                        win, bg_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    value = font.render(str(event.key-48), True, (0, 0, 0))
                    win.blit(value, (position[0]*50+15, position[1]*50))
                    grid_alterada[i-1][j-1] = event.key-48
                    pygame.display.update()
                return
            return


def main():  # FUNÇÃO PRINCIPAL
    global grid, grid_alterada, grid_original, dificuldade, solucao, solution, bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9
    pygame.init()
    win = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Sudoku")
    win.fill(bg_color)
    font = pygame.font.SysFont('Comic Sans MS', 35)
# botao NOVO
    retangulo_novo = pygame.Rect(50, 0, 100, 50)
    pygame.draw.rect(win, (0, 0, 250), retangulo_novo)
    botao_novo = font.render('novo', True, (255, 255, 255))
    win.blit(botao_novo, (50, 0))
# botao SOLUÇÃO
    retangulo_solucao = pygame.Rect(380, 0, 120, 50)
    pygame.draw.rect(win, (0, 0, 250), retangulo_solucao)
    botao_solucao = font.render('solução', True, (255, 255, 255))
    win.blit(botao_solucao, (380, 0))
# texto dificuldade
    texto_dificuldade = font.render('dificuldade', True, (0, 0, 50))
    win.blit(texto_dificuldade, (0, 500))
# botao LIMPAR
    retangulo_limpar = pygame.Rect(200, 0, 120, 50)
    pygame.draw.rect(win, (0, 0, 250), retangulo_limpar)
    botao_limpar = font.render('limpar', True, (255, 255, 255))
    win.blit(botao_limpar, (200, 0))
# botões dificuldaddes
    rect_dif_1 = pygame.Rect(200, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif1, rect_dif_1)
    texto_dif_1 = font.render('1', True, (0, 0, 0))
    win.blit(texto_dif_1, (200, 500))

    rect_dif_2 = pygame.Rect(230, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif2, rect_dif_2)
    texto_dif_2 = font.render('2', True, (0, 0, 0))
    win.blit(texto_dif_2, (230, 500))

    rect_dif_3 = pygame.Rect(260, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif3, rect_dif_3)
    texto_dif_3 = font.render('3', True, (0, 0, 0))
    win.blit(texto_dif_3, (260, 500))

    rect_dif_4 = pygame.Rect(290, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif4, rect_dif_4)
    texto_dif_4 = font.render('4', True, (0, 0, 0))
    win.blit(texto_dif_4, (290, 500))

    rect_dif_5 = pygame.Rect(320, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif5, rect_dif_5)
    texto_dif_5 = font.render('5', True, (0, 0, 0))
    win.blit(texto_dif_5, (320, 500))

    rect_dif_6 = pygame.Rect(350, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif6, rect_dif_6)
    texto_dif_6 = font.render('6', True, (0, 0, 0))
    win.blit(texto_dif_6, (350, 500))

    rect_dif_7 = pygame.Rect(380, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif7, rect_dif_7)
    texto_dif_7 = font.render('7', True, (0, 0, 0))
    win.blit(texto_dif_7, (380, 500))

    rect_dif_8 = pygame.Rect(410, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif8, rect_dif_8)
    texto_dif_8 = font.render('8', True, (0, 0, 0))
    win.blit(texto_dif_8, (410, 500))

    rect_dif_9 = pygame.Rect(440, 510, 25, 30)
    pygame.draw.rect(win, bg_color_dif9, rect_dif_9)
    texto_dif_9 = font.render('9', True, (0, 0, 0))
    win.blit(texto_dif_9, (440, 500))

# DESENHAR A GRELHA
    for i in range(0, 10):
        if (i % 3 == 0):
            grossura_linha = 4
        else:
            grossura_linha = 2
        # desenhar linhas verticais da grelha
        pygame.draw.line(win, (0, 0, 0), (50+50*i, 50),
                         (50+50*i, 500), grossura_linha)
        # desenhar linhas horizonrais da grelha
        pygame.draw.line(win, (0, 0, 0), (50, 50+50*i),
                         (500, 50+50*i), grossura_linha)
    pygame.display.update()  # sem esta linha não aparece nada na janela. Fica tudo preto

# DESENHAR OS NUMEROS
    if solucao == 0:
        # CRIA UM NOVO PUZZLE
        # definir nova grid(após clicar em 'novo')
        grid = sudokum.generate(mask_rate=(dificuldade))
        # sudoku mais dificil do mundo:
    #     grid=[[8,0,0,0,0,0,0,0,0],
        #   [0,0,3,6,0,0,0,0,0],
        #   [0,7,0,0,9,0,2,0,0],

        #   [0,5,0,0,0,7,0,0,0],
        #   [0,0,0,0,4,5,7,0,0],
        #   [0,0,0,1,0,0,0,3,0],

        #   [0,0,1,0,0,0,0,6,8],
        #   [0,0,8,5,0,0,0,1,0],
        #   [0,9,0,0,0,0,4,0,0]]

        # CRIA AS VARIÁVEIS grid_original e grid_alterada a partir da grid
        grid_original = [[grid[x][y]
                          for y in range(len(grid[0]))] for x in range(len(grid))]
        grid_alterada = [[grid[x][y]
                          for y in range(len(grid[0]))] for x in range(len(grid))]

        # INSERE OS VALORES DO PUZZLE NA GRELHA
        for i in range(0, len(grid[0])):
            for j in range(0, len(grid[0])):
                if (0 < grid[i][j] < 10):
                    value = font.render(
                        str(grid[i][j]), True, grid_element_color)
                    win.blit(value, ((j+1)*50+15, (i+1)*50))

        pygame.display.update()

# DESENHAR A SOLUCAO
    if solucao == 1:
        # SE HOUVER SOLUCAO MOSTRA A SOLUCAO
        if solution[0] == True:
            for i in range(0, len(solution[1][0])):
                for j in range(0, len(solution[1][0])):
                    if (0 < solution[1][i][j] < 10):
                        value = font.render(
                            str(solution[1][i][j]), True, grid_element_color)
                        win.blit(value, ((j+1)*50+15, (i+1)*50))

        # SE NAO HOUVER SOLUCAO MOSTRA A GRID ORIGINAL E MENSAGEM S/SOLUCAO
        if solution[0] == False:
            for i in range(0, len(grid[0])):
                for j in range(0, len(grid[0])):
                    if (0 < grid[i][j] < 10):
                        value = font.render(
                            str(grid[i][j]), True, grid_element_color)
                        win.blit(value, ((j+1)*50+15, (i+1)*50))

            rect_sem_solucao = pygame.Rect(340, 0, 40, 50)
            pygame.draw.rect(win, (255, 0, 255), rect_sem_solucao)
            texto_sem_solucao = font.render('s/', True, (255, 255, 255))
            win.blit(texto_sem_solucao, (340, 0))

        pygame.display.update()

        # SE INTRODUZIRMOS OS NUMEROS À MÃO E HOUVER SOLUÇÃO
        if dificuldade == 1 and solution[0] == True:

            for i in range(0, len(solution[1][0])):
                for j in range(0, len(solution[1][0])):
                    if (0 < solution[1][i][j] < 10):
                        value = font.render(
                            str(solution[1][i][j]), True, grid_element_color)
                        win.blit(value, ((j+1)*50+15, (i+1)*50))
            pygame.display.update()
        # SE INTRODUZIRMOS OS NUMEROS À MÃO E NÃO HOUVER SOLUÇÃO (nb ainda nao dá porque nao consegue chegar aqui)
        if dificuldade == 1 and solution[0] == False:

            for i in range(0, len(grid_alterada[0])):
                for j in range(0, len(grid_alterada[0])):
                    if (0 < grid_alterada[i][j] < 10):
                        value = font.render(
                            str(grid_alterada[i][j]), True, grid_element_color)
                        win.blit(value, ((j+1)*50+15, (i+1)*50))

            rect_sem_solucao = pygame.Rect(340, 0, 40, 50)
            pygame.draw.rect(win, (255, 0, 255), rect_sem_solucao)
            texto_sem_solucao = font.render('s/', True, (255, 255, 255))
            win.blit(texto_sem_solucao, (340, 0))

    while True:
        # definição das coordenadas (x, y) do rato
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # fecha a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # verifica as ações do rato
            if event.type == pygame.MOUSEBUTTONUP:
                insert(win, (mouse[0]//50, mouse[1]//50))
                # SE CLICA NO BOTÃO "NOVO"
                if (retangulo_novo[0] <= mouse[0] <= retangulo_novo[0]+retangulo_novo[2]) and (retangulo_novo[1] <= mouse[1] <= retangulo_novo[1]+retangulo_novo[3]):
                    # novo_sudoku()
                    solucao = 0
                    main()  # vai ao main e cria uma nova grid com novos numeros
                # SE CLICA NO BOTÃO "SOLUÇÃO"
                if (solucao == 0 and retangulo_solucao[0] <= mouse[0] <= retangulo_solucao[0]+retangulo_solucao[2]) and (retangulo_solucao[1] <= mouse[1] <= retangulo_solucao[1]+retangulo_solucao[3]):

                    solucao = 1
                    # se os valores tiverem sido introduzidos automaticamente
                    if dificuldade != 1:
                        solution = sudokum.solve(grid)
                        print('grid:')
                        print(grid)
                        print('existe solucao?')
                        print(solution[0])
                    # se os valores tiverem sido introduzidos manualmente
                    if dificuldade == 1:

                        print(sudokum.check(grid_alterada))
                        # DÁ ERRO AQUI SE EU INSERIR VALORES IMPOSSIVEIS como dois 1 na mesma linha, mas nao dá erro se for ele a resolver e der dois 1 na mesma linha, nesse caso dá falso.
                        solution = sudokum.solve(grid_alterada)
                        print('grid alterada:')
                        print(grid_alterada)
                        print('existe solucao?')
                        print(solution[0])

                    main()
                # SE CLICA NO BOTÃO "LIMPAR"
                if (retangulo_limpar[0] <= mouse[0] <= retangulo_limpar[0]+retangulo_limpar[2]) and (retangulo_limpar[1] <= mouse[1] <= retangulo_limpar[1]+retangulo_limpar[3]):
                    # novo_sudoku()
                    dificuldade = 1  # colocar a dificuldade a 1 é igual a limpar a grelha porque fica vazia
                    solucao = 0  # fazer reset à solução
                    # fazer reset às cores dos botões das dificuldades
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                    main()

                # definir se estamos a clicar nos botões da dificuldade
                if rect_dif_1[0] <= mouse[0] <= rect_dif_1[0] + rect_dif_1[2] and rect_dif_1[1] <= mouse[1] <= rect_dif_1[1] + rect_dif_1[3]:
                    dificuldade = 0.1
                    bg_color_dif1 = (0, 100, 255)
                    bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_2[0] <= mouse[0] <= rect_dif_2[0] + rect_dif_2[2] and rect_dif_2[1] <= mouse[1] <= rect_dif_2[1] + rect_dif_2[3]:
                    dificuldade = 0.2
                    bg_color_dif2 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_3[0] <= mouse[0] <= rect_dif_3[0] + rect_dif_3[2] and rect_dif_3[1] <= mouse[1] <= rect_dif_3[1] + rect_dif_3[3]:
                    dificuldade = 0.3
                    bg_color_dif3 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_4[0] <= mouse[0] <= rect_dif_4[0] + rect_dif_4[2] and rect_dif_4[1] <= mouse[1] <= rect_dif_4[1] + rect_dif_4[3]:
                    dificuldade = 0.4
                    bg_color_dif4 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_5[0] <= mouse[0] <= rect_dif_5[0] + rect_dif_5[2] and rect_dif_5[1] <= mouse[1] <= rect_dif_5[1] + rect_dif_5[3]:
                    dificuldade = 0.5
                    bg_color_dif5 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif6, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_6[0] <= mouse[0] <= rect_dif_6[0] + rect_dif_6[2] and rect_dif_6[1] <= mouse[1] <= rect_dif_6[1] + rect_dif_6[3]:
                    dificuldade = 0.6
                    bg_color_dif6 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif7, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_7[0] <= mouse[0] <= rect_dif_7[0] + rect_dif_7[2] and rect_dif_7[1] <= mouse[1] <= rect_dif_7[1] + rect_dif_7[3]:
                    dificuldade = 0.7
                    bg_color_dif7 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif8, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_8[0] <= mouse[0] <= rect_dif_8[0] + rect_dif_8[2] and rect_dif_8[1] <= mouse[1] <= rect_dif_8[1] + rect_dif_8[3]:
                    dificuldade = 0.8
                    bg_color_dif8 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif9 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)
                if rect_dif_9[0] <= mouse[0] <= rect_dif_9[0] + rect_dif_9[2] and rect_dif_9[1] <= mouse[1] <= rect_dif_9[1] + rect_dif_9[3]:
                    dificuldade = 0.9
                    bg_color_dif9 = (0, 100, 255)
                    bg_color_dif1, bg_color_dif2, bg_color_dif3, bg_color_dif4, bg_color_dif5, bg_color_dif6, bg_color_dif7, bg_color_dif8 = (
                        0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255), (0, 200, 255)


main()
