import sys, pygame as pg

pg.init()
screen_size = 750, 750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 80)

# number_grid =[
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
# number_grid = [[3, 9, 1, 8, 5, 6, 4, 2, 7], [8, 6, 7, 2, 3, 4, 9, 1, 5], [4, 2, 5, 7, 1, 9, 6, 8, 3], [7, 5, 4, 9, 6, 8, 1, 3, 2], [2, 1, 6, 4, 7, 3, 5, 9, 8], [9, 3, 8, 5, 2, 1, 7, 6, 4], [5, 4, 3, 6, 9, 2, 8, 7, 1], [6, 7, 2, 1, 8, 5, 3, 
# 4, 9], [1, 8, 9, 3, 4, 7, 2, 5, 6]]
number_grid=[[8, 1, 2, 7, 5, 3, 6, 4, 9], [9, 4, 3, 6, 8, 2, 1, 7, 5], [6, 7, 5, 4, 9, 1, 2, 8, 3], [1, 5, 4, 2, 3, 7, 8, 9, 6], [3, 6, 9, 8, 4, 5, 7, 2, 1], [2, 8, 7, 1, 6, 9, 5, 3, 4], [5, 2, 1, 9, 7, 4, 3, 6, 8], [4, 3, 8, 5, 2, 6, 9, 
1, 7], [7, 9, 6, 3, 1, 8, 4, 5, 2]]
def draw_background():
    screen.fill(pg.Color("white"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720: #desenha desde i=0 até i=8, nao desenha quando i=9 porque 9*80=720 e tem de ser menor que 720
        line_width = 5 if i % 3 > 0 else 10 #se nao for divisível por 3 a linha tem grossura 5, senão tem 10
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i*80)+15, 15), pg.Vector2((i*80)+15, 735), line_width) #definir a cor, o ponto inicial e o ponto final da linha, e a grossura
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i*80)+15), pg.Vector2(735, (i*80)+15), line_width)
        i += 1
def draw_numbers():
    row = 0
    offset = 35
    while row < 9:
        col = 0
        while col < 9:
            output = number_grid[row][col]
            #print(str(output))
            n_text = font.render(str(output), True, pg.Color("black"))
            screen.blit(n_text, pg.Vector2((col*80)+offset+5, (row*80)+offset-2))
            col += 1
        row += 1

def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
    draw_background()
    draw_numbers()
    pg.display.flip() #Update the full display Surface to the screen
while 1:
    game_loop()