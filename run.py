import random

def create_grid(size):
    """
    Will create an empty grid for the game
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

    def print_grid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * (4 * len(row) - 1))

       
def place_ships(grid, num_ships):
    """
    Will place the ships randomly on the grid
    """
    for _ in range(num_ships):
        ship_row = random.randint(0, len(grid) - 1)
        ship_col = random.randint(0, len(grid[0]) - 1)
        while grid[ship_row][ship_col] == 'S':
            ship_row = random.randint(0, len(grid) - 1)
            ship_col = random.randint(0, len(grid[0]) - 1)
        grid[ship_row][ship_col] = 'S'

        