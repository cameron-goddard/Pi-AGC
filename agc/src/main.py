try:
    import RPi.GPIO as GPIO
except ImportError:
    pass

import sys
sys.path.append(sys.path[0] + '/..')
from progs import misc, add_sub, tic_tac_toe, update_curr_time
from dsky import DSKY

if __name__ == "__main__":
    dsky = DSKY()
    progs = [tic_tac_toe.tictactoe, misc.ece, misc.echo, add_sub.add_sub, update_curr_time]
    dsky.init_progs(progs)
   
    if "RPi.GPIO" in sys.modules:
        GPIO.setmode(GPIO.BCM)

        #pins = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27]
        pins = [14, 17, 19]
        for pin in pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(14, GPIO.FALLING, callback=dsky.noun_keyed, bouncetime=400)
        GPIO.add_event_detect(19, GPIO.FALLING, callback=dsky.verb_keyed, bouncetime=400) # reset
        GPIO.add_event_detect(17, GPIO.FALLING, callback=dsky.prog_keyed, bouncetime=400)

    dsky.start()