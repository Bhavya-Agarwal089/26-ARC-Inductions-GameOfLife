#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    
    # TODO: Implement your neighbor-counting logic here!
     


               
    if row==0 and col!= 0 and col!=(len(grid[0])-1):
        for i in range(0,2):
                for j in range (col-1,col+2):
                    if i ==row and j == col :
                       continue
                    else:
                        if grid[i][j] == 1:
                            alive_count += 1


    elif row==(len(grid)-1) and col!= 0 and col!=(len(grid[0])-1):
            for i in range(row-1,row+1):
                    for j in range (col-1,col+2):
                        if i ==row and j == col :
                           continue
                        else:
                            if grid[i][j] == 1:
                                alive_count += 1

    elif row!=0 and row!=(len(grid)-1) and col ==0:
                for i in range(row-1,row+2):
                        for j in range (col,col+2):
                            if i ==row and j == col :
                               continue
                            else:
                                if grid[i][j] == 1:
                                    alive_count += 1

    elif col==(len(grid[0])-1) and row != 0 and row != (len(grid)-1):
                for i in range(row-1,row+2):
                        for j in range (col-1,col+1):
                            if i ==row and j == col :
                               continue
                            else:
                                if grid[i][j] == 1:
                                    alive_count += 1

    elif row==0 and col == 0:
                for i in range(0,2):
                        for j in range (0,2):
                            if i ==row and j == col :
                               continue
                            else:
                                if grid[i][j] == 1:
                                    alive_count += 1
    elif row==0 and col == (len(grid[0])-1):
                    for i in range(0,2):
                            for j in range (col-1,col+1):
                                if i ==row and j == col :
                                   continue
                                else:
                                    if grid[i][j] == 1:
                                        alive_count += 1

    elif row==(len(grid)-1) and col == 0:
                    for i in range(row-1,row+1):
                            for j in range (col,col+2):
                                if i ==row and j == col :
                                   continue
                                else:
                                    if grid[i][j] == 1:
                                        alive_count += 1

    elif row==(len(grid)-1) and col == (len(grid[0])-1):
                    for i in range(row-1,row+1):
                            for j in range (col-1,col+1):
                                if i ==row and j == col :
                                   continue
                                else:
                                    if grid[i][j] == 1:
                                        alive_count += 1

    else:
        for i in range(row-1,row+2):
            for j in range (col-1,col+2):
                if i ==row and j == col :
                   continue
                else:
                    if grid[i][j] == 1:
                        alive_count += 1
                      
    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # TODO: Iterate through every cell in the `grid`.
    # TODO: Use your `count_neighbors` function to find out how many neighbors it has.
    # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.
    

    for i in range(rows):
        for j in range(cols):
               if grid[i][j] == 1:
                   if count_neighbors(grid,i,j) == 2 or count_neighbors(grid,i,j) == 3:
                       next_grid[i][j] = 1
                   else:
                       next_grid[i][j] = 0
               elif grid[i][j] == 0:
                    if count_neighbors(grid,i,j) == 3:
                        next_grid[i][j] = 1
                    else:
                        next_grid[i][j] = 0
    return next_grid
