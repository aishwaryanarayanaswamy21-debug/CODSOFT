import math

def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(board, player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw(board):
    return " " not in board

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def ai_move(board):
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def player_move(board):
    while True:
        try:
            position = int(input("Enter position (1-9): ")) - 1

            if 0 <= position <= 8 and board[position] == " ":
                board[position] = "X"
                break
            else:
                print("Invalid move!")

        except:
            print("Enter a number from 1 to 9.")

def show_positions():
    print("\nBoard Positions\n")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")


board = [" "] * 9

print("===== TIC TAC TOE AI =====")
print("You are X")
print("AI is O")

show_positions()

while True:
    print_board(board)

    player_move(board)

    if check_winner(board, "X"):
        print_board(board)
        print("You Win!")
        break

    if is_draw(board):
        print_board(board)
        print("Game Draw!")
        break

    print("AI is thinking...")

    ai_move(board)

    if check_winner(board, "O"):
        print_board(board)
        print("AI Wins!")
        break

    if is_draw(board):
        print_board(board)
        print("Game Draw!")
        break