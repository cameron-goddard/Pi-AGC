import RPi.GPIO as GPIO
import time
import subprocess

# set up GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO27_callback(channel):
        send = "echo pause > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)

def GPIO23_callback(channel):
        send = "echo seek 10 > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)

def GPIO22_callback(channel):
        send = "echo seek -10 > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)

def GPIO13_callback(channel):
        send = "echo seek 30 > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)

def GPIO26_callback(channel):
        send = "echo seek -30 > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)

def GPIO17_callback(channel):
        send = "echo stop > /home/pi/lab2/video_fifo"
        subprocess.check_output(send, shell=True)


GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback)
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback)
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback)
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback)
GPIO.add_event_detect(13, GPIO.FALLING, callback=GPIO13_callback)
GPIO.add_event_detect(26, GPIO.FALLING, callback=GPIO26_callback)

while True:
    continue

GPIO.cleanup()