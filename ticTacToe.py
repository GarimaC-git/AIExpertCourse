import random
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def display_board(board):
    print()

    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(" " + colored(board[0]) + " | " + colored(board[1]) + " | " + colored(board[2]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + colored(board[3]) + " | " + colored(board[4]) + " | " + colored(board[5]))
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(" " + colored(board[6]) + " | " + colored(board[7]) + " | " + colored(board[8]))
    print()


def player_choice():
    while True:
        symbol = input(Fore.GREEN + "Choose your symbol (X/O): " + Style.RESET_ALL).strip().upper()
        if symbol in ["X", "O"]:
            break
        print(Fore.RED + "Please choose either X or O.")

    if symbol == "X":
        return "X", "O"
    else:
        return "O", "X"


def player_move(board, symbol):
    while True:
        try:
            move = int(input(Fore.GREEN + "Choose a position (1-9): " + Style.RESET_ALL))

            if move not in range(1, 10):
                print(Fore.RED + "Please choose a number between 1 and 9.")
            elif not board[move - 1].isdigit():
                print(Fore.RED + "That position is already occupied.")
            else:
                board[move - 1] = symbol
                break

        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")


def check_win(board, symbol):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == symbol:
            return True
    return False


def ai_move(board, ai_symbol, player_symbol):

    # Try to win
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = ai_symbol
            if check_win(temp, ai_symbol):
                board[i] = ai_symbol
                return

    # Block player
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = player_symbol
            if check_win(temp, player_symbol):
                board[i] = ai_symbol
                return

    # Random move
    empty_positions = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(empty_positions)] = ai_symbol


def check_full(board):
    return all(not cell.isdigit() for cell in board)


def tic_tac_toe():
    print(Fore.CYAN + "===== Welcome to AI Tic-Tac-Toe =====")

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL).strip()

    if not player_name:
        player_name = "Player"

    while True:
        board = [str(i) for i in range(1, 10)]

        player_symbol, ai_symbol = player_choice()

        turn = "Player"

        while True:
            display_board(board)

            if turn == "Player":
                player_move(board, player_symbol)

                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations, {player_name}! You won the game!")
                    break

                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "The game ended in a draw.")
                    break

                turn = "AI"

            else:
                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "The AI wins this round!")
                    break

                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "The game ended in a draw.")
                    break

                turn = "Player"

        play_again = input(
            Fore.GREEN + "Would you like to play again? (yes/no): " + Style.RESET_ALL
        ).strip().lower()

        if play_again != "yes":
            print(Fore.CYAN + "Thanks for playing AI Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    tic_tac_toe()