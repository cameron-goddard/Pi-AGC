import sys
sys.path.append(sys.path[0] + '/..')
from src.dsky import DSKY
import src.util

value = 0
def add_sub(dsky: DSKY, input: str) -> int:
    global value
    if input == None:
        value = 0
        dsky.display.update_row(2, "+++++")
        dsky.display.update_row(1, "-----")
        dsky.display.update_row(0, "+++++")
    elif input == "+" or input == "=":
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
    
    dsky.display.update_noun(src.util.double_str(value))
    return -2