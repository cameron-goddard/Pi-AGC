from dsky import DSKY
#import RPi.GPIO as GPIO
import pygame

def test_prog(dsky: DSKY) -> None:
    dsky.foo()

def idle(dsky: DSKY) -> None:
    while (True):
        continue

def tictactoe(dsky: DSKY) -> None:
    board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    winner = None

    def draw_board():
        dsky.display.update_row(2, "{}{}{}  ".format(board[0], board[1], board[2]))
        dsky.display.update_row(1, "{}{}{}  ".format(board[3], board[4], board[5]))
        dsky.display.update_row(0, "{}{}{}  ".format(board[6], board[7], board[8]))

    def get_player_move():
        while True:
            move = input(f"{current_player}, enter your move (1-9): ")
            if move.isdigit() and int(move) in range(1, 10):
                index = int(move) - 1
                if board[index] == " ":
                    return index
            print("Invalid move. Try again.")

    def check_for_winner():
        nonlocal winner
        for i in range(0, 9, 3):
            if board[i] != " " and board[i] == board[i+1] and board[i+1] == board[i+2]:
                winner = board[i]
                return True
        for i in range(3):
            if board[i] != " " and board[i] == board[i+3] and board[i+3] == board[i+6]:
                winner = board[i]
                return True
        if board[0] != " " and board[0] == board[4] and board[4] == board[8]:
            winner = board[0]
            return True
        if board[2] != " " and board[2] == board[4] and board[4] == board[6]:
            winner = board[2]
            return True
        if " " not in board:
            winner = "tie"
            return True
        return False
    
    #while not check_for_winner():
    draw_board()
    #index = get_player_move()
    #board[index] = current_player
    #current_player = "O" if current_player == "X" else "X"
    
    draw_board()
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins!")



if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    GPIO.setmode(GPIO.BCM)

    pins = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 26, 27]

    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    dsky = DSKY()
    progs = [test_prog, tictactoe]
    dsky.init_progs(progs)

    dsky.start()