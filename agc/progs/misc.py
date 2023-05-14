import sys
sys.path.append(sys.path[0] + '/..')
from src.dsky import DSKY
import src.util

def ece(dsky: DSKY, input: str) -> int:
    dsky.display.update_row(2, "ILOVE")
    dsky.display.update_row(1, "ECE")
    dsky.display.update_row(0, "5725")
    return 0

def echo(dsky: DSKY, input: str) -> int:
    if input == None:
        return -2

    if input == "return":
        return 0

    if input.isdigit():
        dsky.display.update_noun(src.util.double_str(int(input)))
    elif input == "-":
        dsky.display.update_noun("-")
    elif input == "+":
        dsky.display.update_noun("+")