try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
import sys

class Indicators:
    """
    Handles updates to the left-hand side status indicators.
    """

    def __init__(self) -> None:
        self.led_dict = {"TEMP": 12, "PROG": 1, "OPR ERR": 16}
        if "RPi.GPIO" in sys.modules:
            GPIO.setmode(GPIO.BCM)
        
            GPIO.setup(12, GPIO.OUT, initial = GPIO.LOW)
            GPIO.setup(1, GPIO.OUT, initial = GPIO.LOW)
            GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW)   

    def clear_all(self) -> None:
        if "RPi.GPIO" in sys.modules:
            for pin in self.led_dict.values():
                GPIO.output(pin, GPIO.LOW)
    
    def indicator_on(self, val: str) -> None:
        pin = self.led_dict[val]
        if "RPi.GPIO" in sys.modules:
            GPIO.output(pin, GPIO.HIGH)
    
    def indicator_off(self, val: str) -> None:
        pin = self.led_dict[val]
        if "RPi.GPIO" in sys.modules:
            GPIO.output(pin, GPIO.LOW)
    
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
    1 - prog
    2
    3
    4
    7
    8
    10
    12 - temp
    16 - opp err
    18
"""