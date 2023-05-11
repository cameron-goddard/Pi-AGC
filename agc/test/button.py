import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def GPIO17_callback(channel):
        print("17")


GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback)


while True:
    continue

GPIO.cleanup()