# Create an empty board
board = []
for i in range(9):
    board.append(' ')

# Display the board
def print_board():

    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
  

# Check for winner
def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Game loop
current_player = 'X'
moves = 0
print("🎮 Welcome to Tic Tac Toe")
print("Positions are 1 to 9 as below:")
print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")

while moves < 9:
    print_board()
    try:
        choice = int(input(f"{current_player}'s turn. Enter position (1-9): ")) - 1
        if board[choice] == ' ':
            board[choice] = current_player
            moves += 1

            if check_winner(current_player):
                print_board()
                print(f"🏆 Player {current_player} wins!")
                break

            # Switch player
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        else:
            print("⚠️ Spot already taken! Try again.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Choose number between 1-9.")

else:
    print_board()
    print("🤝 It's a draw!")
