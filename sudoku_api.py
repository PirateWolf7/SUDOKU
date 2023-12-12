# import requests
from sudoku import Sudoku
# response = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
#https://sugoku.onrender.com/board
#grid = response.json()['newboard']
#print(len(grid[0]))
#grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


puzzle=Sudoku(3).difficulty(0.7)
puzzle.show()