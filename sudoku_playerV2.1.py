
import requests
import sudokum
#response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
#response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
#response = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
#response = requests.get("https://sugoku.onrender.com/board")
#grid = response.json()['newboard']
grid=sudokum.generate(mask_rate=0.7)

# grid = [[0,0,0,0,0,5,0,0,8],
#         [0,0,0,4,0,0,0,9,2],
#         [0,0,0,6,0,0,4,0,0],
#         [0,9,0,0,2,0,0,7,0],
#         [0,0,7,0,0,6,0,0,9],
#         [0,0,5,7,0,3,0,4,0],
#         [0,0,2,0,0,0,9,0,7],
#         [7,0,9,8,0,0,0,0,4],
#         [0,8,0,0,7,4,2,0,0]] # a API dá erro então usei isto
print(grid)
print(grid[0]) # isto dá a primeira linha
print(grid[1][3]) # isto dá o 4 que está na segunda linha e quarta coluna (NB: isto começa no zero)
print(len(grid[0])) #isto dá 9 que é o tamanho da linha 1
#por isso quando dá erro em range(len(grid[0])) é porque a API nao funciona desta forma mas tem de haver outra solução
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
