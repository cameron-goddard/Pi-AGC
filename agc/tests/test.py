import RPi.GPIO as GPIO


def foo(channel):
    print("here")

GPIO.setmode(GPIO.BCM)

pins = [0, 14, 17, 19]

for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(14, GPIO.FALLING, callback=foo)
GPIO.add_event_detect(19, GPIO.FALLING, callback=foo)
GPIO.add_event_detect(17, GPIO.FALLING, callback=foo)

while True:
    if (not GPIO.input(0)):
        print("0")

