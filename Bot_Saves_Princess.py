def displayPathtoPrincess(n,grid):    
    
    # Get bot position and pricess position
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_cell = (i,j)
            elif grid[i][j] == 'm':
                bot_cell = (i,j)
    drow = bot_cell[0] - princess_cell[0]
    dcol = bot_cell[1] - princess_cell[1]
    
    if drow < 0:
        [print("DOWN") for i in range(abs(drow))]
    if drow > 0:
        [print("UP") for i in range(drow)]
    if dcol < 0:
        [print("RIGHT") for i in range(abs(dcol))]
    if dcol > 0:
        [print("LEFT") for i in range(dcol)]

    return

       
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
