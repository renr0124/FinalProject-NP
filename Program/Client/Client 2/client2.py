
from socket import *

serverName = '47.18.60.15'
serverPort = 25569
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

win_x = 0
win_o = 0
tie_count = 0
win_o_bool = False
win_x_bool = False

# Start Do-While
while True:

    # <Define Functions>
    def print_grid():
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")
        return


    def is_tie(board):
        if board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and board[6] != 7 and board[7] != 8 and board[8] != 9:
            return True
        else:
            return False
    game = True

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    mark = " "


    def print_game():
        print(board[0], " |", board[1], "|", board[2])
        print("---|---|---")
        print(board[3], " |", board[4], "|", board[5])
        print("---|---|---")
        print(board[6], " |", board[7], "|", board[8])
        print()


    def is_legal(mark, board):
        if (board[mark - 1] != mark):
            return False
        else:
            return True

    # 012 | 345 | 678 | 036 | 147 | 258 | 048 | 246
    def win_check(mark, board):
        if((board[0] == mark and board[1] == mark and board[2] == mark) or
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
    # </Define Function>

    # Start
    while(game):
        mark = 'X'

        # Receive from Server
        oppInput = clientSocket.recv(1024)
        oppInput = int(oppInput)
        board[oppInput - 1] = mark

        print_game()

        # Check game status
        if (win_check(mark, board)):
            print("The winner is " + mark)
            if mark == 'X':
                win_x = win_x + 1
                win_x_bool = True
            elif mark == 'O':
                win_o_bool = True
                win_o = win_o + 1
            print("X Has won " + str(win_x))
            print("O Has won " + str(win_o))
            print("There have been " + str(tie_count) + " ties.")
            game = False
            break

        if (is_tie(board)):
            print("The Match is a tie.")
            tie_count += 1
            print("X Has won " + str(win_x))
            print("O Has won " + str(win_o))
            print("There have been " + str(tie_count) + " ties.")
            game = False
            break

        # Sending to Server

        mark = 'O'

        while True:
            clientInput = input('Enter Value: ')
            user_input = clientInput
            user_input = int(user_input)
            print(user_input)

            if is_legal(user_input, board):
                clientSocket.send(clientInput.encode())
                board[user_input - 1] = mark
                break
            else:
                print("That is not a legal move. Please try again!")

        print_game()

        if (win_check(mark, board)):
            print("The winner is " + mark)
            if mark == 'X':
                win_x_bool = True
                win_x = win_x + 1
            else:
                win_o_bool = True
                win_o = win_o + 1
            print("X Has won " + str(win_x))
            print("O Has won " + str(win_o))
            print("There have been " + str(tie_count) + " ties.")
            game = False
            break

        if (is_tie(board)):
            print("The Match is a tie.")
            tie_count += 1
            print("X Has won " + str(win_x))
            print("O Has won " + str(win_o))
            print("There have been " + str(tie_count) + " ties.")
            game = False
            break

    # Ask to play again
    if win_o_bool:
        useless = clientSocket.recv(1024).decode()
    win_o_bool = False
    answer = input("Would you like to play again? Yes or no.")
    answer = answer.lower()

    # Send answer to Server
    clientSocket.send(answer.encode())

    if answer != "yes":
        print("Have a good day!")
        game = False
        exit()
    else:
        game = True
    game = True
# Break from loop and end if not YES
