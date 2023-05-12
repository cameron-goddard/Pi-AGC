import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
        
GPIO.setup(12, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial = GPIO.LOW)  

while True: # Run forever
    GPIO.output(12, GPIO.HIGH) # Turn on
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1)                  # Sleep for 1 second
    GPIO.output(12, GPIO.LOW)  # Turn off
    GPIO.output(1, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    time.sleep(1)  

GPIO.cleanup()