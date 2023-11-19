import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def get_player_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter integers.")


def get_computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)


def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_symbols = ['X', 'O']
    current_player = 0

    print_board(board)

    while True:
        print(f"Player {current_player + 1}'s turn ({player_symbols[current_player]})")

        if current_player == 0:  # Human player
            row, col = get_player_move()
        else:  # Computer player
            row, col = get_computer_move(board)
            print(f"Computer plays: {row}, {col}")

        if board[row][col] == ' ':
            board[row][col] = player_symbols[current_player]
            print_board(board)

            if check_winner(board, player_symbols[current_player]):
                print(f"Player {current_player + 1} ({player_symbols[current_player]}) wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = 1 - current_player  # Switch players
        else:
            print("Cell already taken. Try again.")


if __name__ == "__main__":
    play_tic_tac_toe()
