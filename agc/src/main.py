from dsky import DSKY
import RPi.GPIO as GPIO
import pygame
import time


def idle(dsky: DSKY) -> None:
    while (True):
        continue

def hello(dsky: DSKY, input: str) -> None:
    dsky.display.update_row(2, "HELLO")
    dsky.display.update_row(1, "PROF")
    dsky.display.update_row(0, "SKOVIR")
    return 0

board = ["+", "+", "+", "+", "+", "+", "+", "+", "+"]
current_player = "0"
winner = None

def tictactoe(dsky: DSKY, input: str) -> int:
    global board, current_player, winner
    print(input)
    
    if input == None:
        dsky.display.update_row(2, "{}{}{}  ".format(board[0], board[1], board[2]))
        dsky.display.update_row(1, "{}{}{}  ".format(board[3], board[4], board[5]))
        dsky.display.update_row(0, "{}{}{}  ".format(board[6], board[7], board[8]))
        return -2
    if board[int(input)-1] == "+":
        board[int(input)-1] = current_player
    else:
        return
    
    dsky.display.update_row(2, "{}{}{}  ".format(board[0], board[1], board[2]))
    dsky.display.update_row(1, "{}{}{}  ".format(board[3], board[4], board[5]))
    dsky.display.update_row(0, "{}{}{}  ".format(board[6], board[7], board[8]))
    
    for i in range(0, 9, 3):
        if board[i] != "+" and board[i] == board[i+1] and board[i+1] == board[i+2]:
            winner = board[i]
    for i in range(3):
        if board[i] != "+" and board[i] == board[i+3] and board[i+3] == board[i+6]:
            winner = board[i]
    if board[0] != "+" and board[0] == board[4] and board[4] == board[8]:
        winner = board[0]
    if board[2] != "+" and board[2] == board[4] and board[4] == board[6]:
        winner = board[2]
    if "+" not in board:
        winner = "tie"
    
    if winner != None:
        if winner == "0":
            dsky.display.update_row(2, "000")
            dsky.display.update_row(1, "0+0")
            dsky.display.update_row(0, "000")
        else:
            dsky.display.update_row(2, "8+8")
            dsky.display.update_row(1, "+8+")
            dsky.display.update_row(0, "8+8")
        return 0
        
    current_player = "8" if current_player == "0" else "0"
    return -2



if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    pygame.mouse.set_visible(0)

    GPIO.setmode(GPIO.BCM)

    pins = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 26, 27]

    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    


    dsky = DSKY()
    progs = [tictactoe, hello]
    dsky.init_progs(progs)

    GPIO.add_event_detect(14, GPIO.FALLING, callback=dsky.noun_keyed)
    GPIO.add_event_detect(20, GPIO.FALLING, callback=dsky.verb_keyed)

    dsky.start()