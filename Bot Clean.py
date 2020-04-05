#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    # greedy position
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    # get dirty cells
    dirty_cells = [(i,j) for i in range(5) for j in range(5) if board[i][j] == 'd']
    
    best_cell = None
    best_distance = float('inf')
    # get best_distance (manhattan)
    for x,y in dirty_cells:
        if abs(posr - x) + abs(posc - y) < best_distance:
            best_distance = abs(posr - x) + abs(posc - y)
            best_cell = (x,y)
    # Get best_cell
    if posr - best_cell[0] < 0:
        print("DOWN")
    elif posr - best_cell[0] > 0:
        print("UP")
    elif posc - best_cell[1] < 0:
        print("RIGHT")
    else:
        print("LEFT")
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
