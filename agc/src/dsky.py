import Rpi.GPIO as GPIO
import time
import keyboard


class DSKY:

    def __init__(self):
        pass

    def run(self):
        while True:
            try:
                if keyboard.is_pressed('v'):
                    print("verb")
            except:
                break
