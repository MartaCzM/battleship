import random

def create_grid(size):
    """
    Will create an empty grid for the game
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_grid(grid):
    """
    The function will print the game grid.
    """
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

def computer_guess(size):
    """
    This code introduces the computer_guess function, which generates a random guess for the computer.
    After the user's guess, the computer's turn is triggered. 
    """
    guess_row = random.randint(0, size - 1)
    guess_col = random.randint(0, size - 1)
    return guess_row, guess_col

def is_ship_sunk(grid, row, col):
    return grid[row][col] == 'X'

def play_game():
    """
    This code represents the main loop of the game.
    """
    grid_size = 5
    num_ships = 3

    user_grid = create_grid(grid_size)
    computer_grid = create_grid(grid_size)

    place_ships(computer_grid, num_ships)

    print("Welcome to Battleships!")
    print("Guess the positions of the computer's ships.")

    while True:
        print("Your grid:")
        print_grid(user_grid)

        user_row, user_col = get_user_guess(grid_size)

        if computer_grid[user_row][user_col] == 'S':
            print("Congratulations! You hit a ship!")
            user_grid[user_row][user_col] = 'X'
        else:
            print("Sorry, it's a miss.")
            user_grid[user_row][user_col] = 'O'

        if all(cell == 'X' for row in user_grid for cell in row):
            print("Congratulations! You sank all the ships!")
            break

        print("Computer's turn:")
        computer_row, computer_col = computer_guess(grid_size)

        if user_grid[computer_row][computer_col] == 'S':
            print("Oh no! The computer hit your ship!")
            user_grid[computer_row][computer_col] = 'X'
        else:
            print("Phew! The computer missed.")
            user_grid[computer_row][computer_col] = 'O'

        if all(cell == 'X' for row in user_grid for cell in row):
            print("Oh no! The computer sank all your ships!")
            break

play_game()