from socket import *

serverName = '47.18.60.15'
serverPort = 25565
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:

    def print_grid():
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")
        return


    def is_tie(mark, board):
        if(board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and board[6] != 7 and board[7] != 8 and board[8] != 9 ):
            return True
        else:
            return False

    # print_grid()


    game = True

    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    mark = " "


    def print_game():
        print(board[0], " |", board[1], "|", board[2])
        print("---|---|---")
        print(board[3], " |", board[4], "|", board[5])
        print("---|---|---")
        print(board[6], " |", board[7], "|", board[8])


    def is_legal(mark, board):
        if(board[mark - 1] != mark):
            return False
        else:
            return True

    # 012 | 345 | 678 | 036 | 147 | 258 | 048 | 246
    def win_check (mark, board):
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


    index = 1
    while(game):

        if(index % 2 == 1):
            mark = 'X'
        else: mark = 'O'

        print_game()
        while True:
            print('Enter value')
            user_input = input()
            user_input = int(user_input)
            if(is_legal(user_input, board)):
                break
            else:
                print("That is not a legal move. Please try again!")
        user_input = user_input - 1

        board[user_input] = mark

        if(is_tie(mark, board)):
            print("The Match is a tie.")
            break
        if(win_check(mark, board)):
            print("The winner is " + mark)
            break
        index = index + 1
    answer = input("Would you like to play again?")
    if(answer.capitalize() != "YES"):
        print("Have a good day!")
        break










