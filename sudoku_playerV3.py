import pygame
import requests
from sudoku import Sudoku

WIDTH = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5
# response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
# response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
#response = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
#https://sugoku.onrender.com/board
#grid = response.json()['newboard']
grid=Sudoku(3).difficulty(0.7)
print(grid)
print(grid[0]) #com o Sudoku não dá para fazer isto



# grid = [[0,0,0,0,0,5,0,0,8],
#         [0,0,0,4,0,0,0,9,2],
#         [0,0,0,6,0,0,4,0,0],
#         [0,9,0,0,2,0,0,7,0],
#         [0,0,7,0,0,6,0,0,9],
#         [0,0,5,7,0,3,0,4,0],
#         [0,0,2,0,0,0,9,0,7],
#         [7,0,9,8,0,0,0,0,4],
#         [0,8,0,0,7,4,2,0,0]] # a API dá erro então usei isto
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i-1][j-1] != 0):
                    return
                if (event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    pygame.display.update()
                if (0<event.key-48<10): #check por input válido
                    pygame.draw.rect(win, background_color, (position[0]*50+buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    value=myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50+15, position[1]*50))
                    grid[i-1][j-1]= event.key-48
                    pygame.display.update()
                return
            return
                    #1. tries do edit original file
                    
                    #2. edit
                    #3. adding the digits

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("SUDOKU")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if (i%3==0):
            grossura=4
        else:
            grossura=2
        pygame.draw.line(win, (0,0,0),(50+50*i, 50),(50+50*i, 500),grossura)
        pygame.draw.line(win, (0,0,0),(50, 50+50*i),(500, 50+50*i),grossura)
    pygame.display.update()
    
    for i in range(0, len(grid[0])): #range(0 a 9(exclusivo))
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 +15, (i+1)*50))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()