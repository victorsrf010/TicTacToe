import math

# Define the game state and possible moves
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
human = 'X'
computer = 'O'

# Define the evaluation function
def evaluate(board):
    if (board[0] == board[1] == board[2] == human or
        board[3] == board[4] == board[5] == human or
        board[6] == board[7] == board[8] == human or
        board[0] == board[3] == board[6] == human or
        board[1] == board[4] == board[7] == human or
        board[2] == board[5] == board[8] == human or
        board[0] == board[4] == board[8] == human or
        board[2] == board[4] == board[6] == human):
        return -1
    elif (board[0] == board[1] == board[2] == computer or
          board[3] == board[4] == board[5] == computer or
          board[6] == board[7] == board[8] == computer or
          board[0] == board[3] == board[6] == computer or
          board[1] == board[4] == board[7] == computer or
          board[2] == board[5] == board[8] == computer or
          board[0] == board[4] == board[8] == computer or
          board[2] == board[4] == board[6] == computer):
        return 1
    else:
        return 0

# Implement the minimax algorithm
def minimax(board, player, depth):
    if player == computer:
        best = [-1, -math.inf]
    else:
        best = [-1, math.inf]

    if depth == 0 or evaluate(board) != 0:
        score = evaluate(board)
        return [-1, score]

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = player
            score = minimax(board, human if player == computer else computer, depth - 1)
            board[i] = ' '
            score[0] = i

            if player == computer:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score

    return best

# Play the game
player = human
humanWins = 0
computerWins = 0
draws = 0
while True:
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    if evaluate(board) != 0:
        if evaluate(board) == 1:
            print("Computer wins!")
            computerWins+=1
        else:
            print("Human wins!")
            humanWins+=1
        restart = input("Do you wish to restart? (y/n): ")
        if restart.lower() == "y":
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            print("Human wins: ", humanWins)
            print("Computer wins: ", computerWins)
            print("Draws: ", draws)

            break
    elif ' ' not in board:
        print("It's a draw!")
        draws+=1
        restart = input("Do you wish to restart? (y/n): ")
        if restart.lower() == "y":
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            continue
        else:
            break

    if player == human:
        while True:
            move = int(input("Enter your move (1-9): "))
            while move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                move = int(input("Enter your move (1-9): "))
            if board[move-1] == ' ':
                board[move-1] = human
                break
            elif move :
                print("Invalid move. Try again.")
    else:
        print("Computer is thinking...")
        move = minimax(board, computer, 9)[0]
        board[move] = computer

    player = human if player == computer else computer
