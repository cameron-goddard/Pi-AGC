try:
    import RPi.GPIO as GPIO
except ImportError:
    pass

from dsky import DSKY
import pygame

value = 0
def add_sub(dsky: DSKY, input: str) -> int:
    global value
    if input == None:
        value = 0
        dsky.display.update_row(2, "+++++")
        dsky.display.update_row(1, "-----")
        dsky.display.update_row(0, "+++++")
    elif input == "+":
        value += 1
        if value == 5:
            dsky.display.update_noun("05")
            return 0
    elif input == "-":
        value -= 1
        if value == -5:
            dsky.display.update_noun("-5")
            return 0
    else:
        return -1
    
    dsky.display.update_noun(double_str(value))
    return -2
    
def ece(dsky: DSKY, input: str) -> int:
    dsky.display.update_row(2, "ILOVE")
    dsky.display.update_row(1, "ECE")
    dsky.display.update_row(0, "5725")
    return 0

secs_seq = []
mins_seq = []
hours_seq = []
curr_seq = "hours"
def update_curr_time(dsky: DSKY, input: str) -> int:
    global secs_seq, mins_seq, hours_seq, curr_seq

    if input == None:
        dsky.display.update_verb("21")
        dsky.display.update_noun("36")
    else:
        if input == "clear":
            if curr_seq == "hours":
                hours_seq = []
            elif curr_seq == "minutes":
                mins_seq = []
            else:
                secs_seq = []

        elif input == "enter":
            if curr_seq == "hours":
                if len(hours_seq) == 5:
                    curr_seq = "minutes"
                else:
                    return -1
            elif curr_seq == "minutes":
                if len(mins_seq) == 5:
                    curr_seq = "seconds"
                    dsky.display.update_row()
                    return -2
                else:
                    return -1
            elif curr_seq == "seconds":
                if len(secs_seq) == 5:
                    #change time
                    #dsky._boot_time = 
                    return 0
                else:
                    return -1
        else:
            num = None
            try:
                num = int(input)
            except ValueError:
                return -1
            if curr_seq == "hours":
                hours_seq.append(num)
            elif curr_seq == "minutes":
                mins_seq.append(num)
            else:
                secs_seq.append(num)


board = ["+", "+", "+", "+", "+", "+", "+", "+", "+"]
current_player = "0"
winner = None

def tictactoe(dsky: DSKY, input: str) -> int:
    global board, current_player, winner
    
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
        elif winner == "8":
            dsky.display.update_row(2, "9+9")
            dsky.display.update_row(1, "+9+")
            dsky.display.update_row(0, "9+9")
        else:
            dsky.display.update_row(2, "333")
            dsky.display.update_row(1, "+3+")
            dsky.display.update_row(0, "+3+")
        return 0
        
    current_player = "9" if current_player == "0" else "0"
    return -2

def double_str(num: int) -> str:
    if num < 10:
        return "0" + str(num)
    return str(num)

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    pygame.mouse.set_visible(0)

    GPIO.setmode(GPIO.BCM)

    #pins = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27]
    pins = [14, 17, 19]
    for pin in pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    


    dsky = DSKY()
    progs = [tictactoe, ece, add_sub, update_curr_time]
    dsky.init_progs(progs)

    GPIO.add_event_detect(14, GPIO.FALLING, callback=dsky.noun_keyed, bouncetime=400)
    GPIO.add_event_detect(19, GPIO.FALLING, callback=dsky.verb_keyed, bouncetime=400) # reset
    GPIO.add_event_detect(17, GPIO.FALLING, callback=dsky.prog_keyed, bouncetime=400)

    dsky.start()