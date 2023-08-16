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


def get_user_guess(size):
    """
    Function that will make the player guesses possible
    """
    while True:
        guess = input(f"Enter your guess (e.g., A3): ").strip().upper()
        if len(guess) != 2 or not guess[0].isalpha() or not guess[1].isdigit():
            print("Invalid input. Please use the format: LetterNumber (e.g., A3)")
            continue

        row = ord(guess[0]) - ord('A')
        col = int(guess[1]) - 1

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Guess is off-grid. Try again.")
            continue

        return row, col