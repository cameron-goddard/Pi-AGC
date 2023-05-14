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
        self.led_dict = {"TEMP": 12, "PROG": 1, "OPR ERR": 16, "KEY REL": 7, "TRACKER": 8, "STBY": 25}
        if "RPi.GPIO" in sys.modules:
            GPIO.setmode(GPIO.BCM)

            for pin in self.led_dict.values():
                GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)

    def clear_all(self) -> None:
        if "RPi.GPIO" in sys.modules:
            for pin in self.led_dict.values():
                GPIO.output(pin, GPIO.LOW)
    
    def indicator_on(self, inds: list[str]) -> None:
        for ind in inds:
            pin = self.led_dict[ind]
            if "RPi.GPIO" in sys.modules:
                GPIO.output(pin, GPIO.HIGH)
    
    def indicator_off(self, inds: list[str]) -> None:
        for ind in inds:
            pin = self.led_dict[ind]
            if "RPi.GPIO" in sys.modules:
                GPIO.output(pin, GPIO.LOW)
    