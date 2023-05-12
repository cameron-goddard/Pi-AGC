import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO2_callback(channel):
        print("2")
def GPIO3_callback(channel):
        print("3")
def GPIO4_callback(channel):
        print("4")
def GPIO17_callback(channel):
        print("17")
def GPIO27_callback(channel):
        print("27")
def GPIO22_callback(channel):
        print("22")
def GPIO10_callback(channel):
        print("10")
def GPIO9_callback(channel):
        print("9")
def GPIO11_callback(channel):
        print("11")
def GPIO0_callback(channel):
        print("0")
def GPIO5_callback(channel):
        print("5")
def GPIO6_callback(channel):
        print("6")
def GPIO13_callback(channel):
        print("13")
def GPIO19_callback(channel):
        print("19")
def GPIO26_callback(channel):
        print("26")
def GPIO14_callback(channel):
        print("14")
def GPIO15_callback(channel):
        print("15")
def GPIO18_callback(channel):
        print("18")
def GPIO23_callback(channel):
        print("23")
def GPIO24_callback(channel):
        print("24")

GPIO.add_event_detect(2, GPIO.FALLING, callback=GPIO2_callback, bouncetime=400)
GPIO.add_event_detect(3, GPIO.FALLING, callback=GPIO3_callback, bouncetime=400)
GPIO.add_event_detect(4, GPIO.FALLING, callback=GPIO4_callback, bouncetime=400)
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=400)
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=400)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=400)
GPIO.add_event_detect(10, GPIO.FALLING, callback=GPIO10_callback, bouncetime=400)
GPIO.add_event_detect(9, GPIO.FALLING, callback=GPIO9_callback, bouncetime=400)
GPIO.add_event_detect(11, GPIO.FALLING, callback=GPIO11_callback, bouncetime=400)
GPIO.add_event_detect(0, GPIO.FALLING, callback=GPIO0_callback, bouncetime=400)
GPIO.add_event_detect(5, GPIO.FALLING, callback=GPIO5_callback, bouncetime=400)
GPIO.add_event_detect(6, GPIO.FALLING, callback=GPIO6_callback, bouncetime=400)
GPIO.add_event_detect(13, GPIO.FALLING, callback=GPIO13_callback, bouncetime=400)
GPIO.add_event_detect(19, GPIO.FALLING, callback=GPIO19_callback, bouncetime=400)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback, bouncetime=400)
GPIO.add_event_detect(14, GPIO.FALLING, callback=GPIO14_callback, bouncetime=400)
GPIO.add_event_detect(15, GPIO.FALLING, callback=GPIO15_callback, bouncetime=400)
GPIO.add_event_detect(18, GPIO.FALLING, callback=GPIO18_callback, bouncetime=400)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=400)
GPIO.add_event_detect(24, GPIO.FALLING, callback=GPIO24_callback, bouncetime=400)


while True:
    continue

GPIO.cleanup()