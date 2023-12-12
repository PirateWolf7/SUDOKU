from pprint import pprint
def find_next_empty(puzzle):
    #2 encontrar os espaços vazios
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1: #puzzle[r][c] retorna o valor que está na linnha r e na coluna c
                return r, c
    return None, None #se nao tiver espaços vazios
#5 verifica se o palpite está certo
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False #se o valor já estiver naquela linha retorna falso
    # col_vals=[]
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals=[puzzle[i][col] for i in range(9)] #list compreension
    if guess in col_vals:
        return False #se o valor já estiver naquela coluna retorna falso
    
    row_start = (row // 3)*3 
    col_start = (col // 3)*3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess: #DEPOIS TESTAR: if guess in puzzle[r][c]
                return False
   
    return True
    
def solve_sudoku(puzzle):
    #1º escolher um quadrado 
    row, col = find_next_empty(puzzle)

    #3 se nao tiver espaços vazios
    if row is None:
        return True #puzzle resolvido
    
    #4 se tiver espaços vazios
    for guess in range(1, 10):
        #5 verifica se o palpite está certo
        if is_valid(puzzle, guess, row, col):
            #6
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True #puzzle resolvido
        #7 voltar a trás
        puzzle[row][col] = -1
    #8 nao tem solução
    return False

if __name__ == '__main__':
    # example_board = [
    #     [3, 9, -1, -1, 5, -1, -1, -1, -1],
    #     [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    #     [-1, -1, -1, 7, 1, 9, -1, 8, -1],

    #     [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    #     [2, -1, 6, -1, -1, 3, -1, -1, -1], 
    #     [-1, -1, -1, -1, -1, -1, -1, -1, 4],

    #     [5, -1, -1, -1, -1, -1, -1, -1, -1], 
    #     [6, 7, -1, 1, -1, 5, -1, 4, -1],
    #     [1, -1, 9, -1, -1, -1, 2, -1, -1]
    # ]
    example_board = [
        [8, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 3, 6, -1, -1, -1, -1, -1],
        [-1, 7, -1, -1, 9, -1, 2, -1, -1],
        
        [-1, 5, -1, -1, -1, 7, -1, -1, -1],
        [-1, -1, -1, -1, 4, 5, 7, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, 3, -1],

        [-1, -1, 1, -1, -1, -1, -1, 6, 8],
        [-1, -1, 8, 5, -1, -1, -1, 1, -1],
        [-1, 9, -1, -1, -1, -1, 4, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
