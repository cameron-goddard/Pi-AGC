import sys
sys.path.append(sys.path[0] + '/..')
from src.dsky import DSKY

secs_seq = []
mins_seq = []
hours_seq = []
curr_seq = "hours"
def update_curr_time(dsky: DSKY, input: str) -> int:
    global secs_seq, mins_seq, hours_seq, curr_seq

    if input == None:
        dsky.display.update_verb("21")
        dsky.display.update_noun("36")
    else:
        if input == "clear":
            if curr_seq == "hours":
                hours_seq = []
            elif curr_seq == "minutes":
                mins_seq = []
            else:
                secs_seq = []

        elif input == "enter":
            if curr_seq == "hours":
                if len(hours_seq) == 5:
                    curr_seq = "minutes"
                else:
                    return -1
            elif curr_seq == "minutes":
                if len(mins_seq) == 5:
                    curr_seq = "seconds"
                    dsky.display.update_row()
                    return -2
                else:
                    return -1
            elif curr_seq == "seconds":
                if len(secs_seq) == 5:
                    #change time
                    #dsky._boot_time = 
                    return 0
                else:
                    return -1
        else:
            num = None
            try:
                num = int(input)
            except ValueError:
                return -1
            if curr_seq == "hours":
                hours_seq.append(num)
            elif curr_seq == "minutes":
                mins_seq.append(num)
            else:
                secs_seq.append(num)