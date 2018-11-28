from socket import *
import tkinter

#TESTING ZONE

serverName = '47.18.60.15'
serverPort = 25565
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Start Do-While
while True:

    # <Defining Functions>

    # prints grid
    def print_grid():
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")
        return

    # check is current game is tie
    def is_tie(board):
        if (board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and
                board[6] != 7 and board[7] != 8 and board[8] != 9):
            return True
        else:
            return False

    # boolean value for game
    game = True

    # array of board entries
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # player mark [X, O]
    mark = " "

    # prints current board with corresponding player marks
    def print_game():
        print(board[0], " |", board[1], "|", board[2])
        print("---|---|---")
        print(board[3], " |", board[4], "|", board[5])
        print("---|---|---")
        print(board[6], " |", board[7], "|", board[8])

    # return True or False depending on if the space Player wants to occupy is already taken
    def is_legal(mark, board):
        if (board[mark - 1] != mark):
            return False
        else:
            return True

    # 012 | 345 | 678 | 036 | 147 | 258 | 048 | 246 <-Ignore
    # iterate through all possible winning combinations and check is winner is determined
    def win_check(mark, board):
        if ((board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                (board[6] == mark and board[7] == mark and board[8] == mark) or
                (board[0] == mark and board[3] == mark and board[6] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[0] == mark and board[4] == mark and board[8] == mark) or
                (board[2] == mark and board[4] == mark and board[6] == mark)
        ):
            return True
        else:
            return False

        # </Defining Functions>

    # START OF GAME
    while (game):

        # Player Mark is X
        mark = 'X'
        # Display the board
        print_game()

        # Start of Loop. Sending to server
        while True:
            clientInput1 = input('Enter Value: ')   # prompt for user to enter value, store at clientInput1
            clientInput = int(clientInput1)         # cast clientInput1 to INTEGER value, stored at clientInput

            if (is_legal(clientInput, board)):      # check if the player entry isLegal:
                clientSocket.send(clientInput1.encode())    # If True, send input to Server, and break from Loop
                board[clientInput - 1] = mark               # Subtract 1 because arrays index at 0
                break
            else:   # If false,  return to Start of Loop and continue until a legal input is provided
                print("That is not a legal move. Please try again!")
        # end loop

        print_game()    # Print Game with clientInput

        # <Game Check>
        # Check for winners. If winner is found, break from game-loop
        if (win_check(mark, board)):
            print("The winner is " + mark)
            game = False
            break
        # Check if game is a tie. If is Tie, break from game-loop
        if (is_tie(board)):
            print("The Match is a tie.")
            game = False
            break
        # </Game Check>

        # Switch to opposing client. Receiving from server
        mark = 'O'     # Mark is changed to O to match corresponding client mark
        clientInput = clientSocket.recv(1024)   # Receive
        clientInput = int(clientInput)          # cast input to INTEGER
        board[clientInput - 1] = mark           # subtract 1 because index at 0, not 1

        print_game()    # display current board with all player marks

        #   check winner
        if (win_check(mark, board)):
            print("The winner is " + mark)
            game = False
            break

        # check tie
        if (is_tie(board)):
            print("The Match is a tie.")
            game = False
            break

    # receive answer to "play again?"
    answer = clientSocket.recv(1024).decode()
    print(answer)
    if(answer != 'yes'):    # if answer is not YES, break from first loop, and end.
        print("Have a good day!")
        game = False
        break
