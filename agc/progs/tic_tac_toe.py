import sys
sys.path.append(sys.path[0] + '/..')
from src.dsky import DSKY

board = ["+", "+", "+", "+", "+", "+", "+", "+", "+"]
current_player = "0"
winner = None

def tictactoe(dsky: DSKY, input: str) -> int:
    global board, current_player, winner
    
    if input == None:
        board = ["+", "+", "+", "+", "+", "+", "+", "+", "+"]
        current_player = "0"
        winner = None
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