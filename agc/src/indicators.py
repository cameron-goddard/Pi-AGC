
#import RPi.GPIO as GPIO
import pygame

class Indicators:
    """
    Handles updates to the left-hand side status indicators.
    """

    def __init__(self) -> None:
        pass

    def clear_all(self) -> None:
        pass
    
    """
    key - gpio
    
    noun - 14
    verb - 20
    0 - 11
    - - 15
    + - 21
    1 - 0
    4 - 18
    7 - 9
    2 - 5
    5 - 23
    8 - 10
    3 - 6
    6 - 24
    9 - 22
    key release - 13
    prog - 17
    clear - 27
    reset - 19
    enter - 26
    
    unused gpios:
    2
    3
    4
    7
    8
    10
    12
    16
    18
"""