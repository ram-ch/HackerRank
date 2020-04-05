

def next_move(posx, posy, dimx, dimy, board):
    # Check if the bot is in dirty cell
    if board[posx][posy] == 'd':
        print('CLEAN')
        return
    
    # Get coordinates of all dirty cells
    dirty_cells = [(i,j) for i in range(dimx) for j in range(dimy) if board[i][j] == 'd']    
    best_cell = None
    best_distance = float('inf')
    # Get the closest cell
    for x,y in dirty_cells:
        if abs(posx - x) + abs(posy - y) < best_distance :
            best_distance = abs(posx - x) + abs(posy - y)
            best_cell = (x,y)
    if posx - best_cell[0] < 0:
        print("DOWN")
    elif posx - best_cell[0] > 0:
        print("UP")
    elif posy - best_cell[1] < 0:
        print("RIGHT")
    else:
        print("LEFT")
            
    return

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
