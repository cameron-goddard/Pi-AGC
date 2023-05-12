import util
from display import Display
from indicators import Indicators

class Parser:
    """
    Reads in sequences of user input and returns a valid command or error.
    Updates the display and indicator lights as appropriate.
    """

    def __init__(self, display: Display, indicators: Indicators) -> None:
        self.display: Display = display
        self.indicators: Indicators = indicators

        self.verb_seq: list[int] = []
        self.noun_seq: list[int] = []

        self.last_action: str = None

    def enter(self, key: str) -> int:
        """
        Handles an input key from the DSKY and returns the status after keystroke

        Args:
            key (str): A valid keystroke

        Returns:
            int: An id for a program, -1 for an error, or -2 for incomplete
        """
        self.__status()
        
        if key == "v":
            self.last_action = "verb"

            if len(self.noun_seq) != 0:
                self.display.clear_all(excluding=["noun"])
            else:
                self.display.clear_all()
            return -2
            
        elif key == "n":
            self.last_action = "noun"
            
            if len(self.verb_seq) != 0:
                self.display.clear_all(excluding=["verb"])
            else:
                self.display.clear_all()
            return -2

        elif key == "program":
            pass
        elif key == "key-release":
            pass
        elif key == "reset":
            pass
        elif key == "-":
            pass
        elif key == "+":
            pass
        elif key == "return":
            if self.last_action == None:
                # TODO: flash opr err indicator
                return -1

            if self.last_action == "prog":
                if len(self.noun_seq) != 2:
                    return -1
                
                self.last_action = None
                temp_seq = self.noun_seq
                self.__clear()
                print("returning prog " + ''.join(str(n) for n in temp_seq))
                return int(''.join(str(n) for n in temp_seq))

            if self.last_action == "verb" and self.verb_seq[0] == 3 and self.verb_seq[1] == 7:
                self.last_action = "prog"
                return -2

            self.last_action = None
            print("going into parse command")
            return self.__parse_commands()
        else:
            # Handle number key
            if len(self.noun_seq) != 0 and len(self.verb_seq) == 0:
                self.display.clear_all(excluding=["prog"])
                return -1
            
            num = int(key)

            if self.last_action == "verb":
                if len(self.verb_seq) < 2:
                    self.verb_seq.append(num)
                    self.display.update_verb(''.join(str(v) for v in self.verb_seq))
            elif self.last_action == "noun":
                if len(self.noun_seq) < 2:
                    self.noun_seq.append(num)
                    self.display.update_noun(''.join(str(v) for v in self.noun_seq))
            elif self.last_action == "prog":
                if len(self.noun_seq) < 2:
                    self.noun_seq.append(num)
                    self.display.update_noun(''.join(str(v) for v in self.noun_seq))
            else:
                self.display.clear_all(excluding=["prog"])
            return -2
                
    def __clear(self) -> None:
        self.verb_seq = []
        self.verb = False

        self.noun_seq = []
        self.noun = False

    def __parse_commands(self) -> int:
        ret = -1
        for comm in util.commands:
            if comm[0] == self.__str__():
                ret = comm[1]
        self.__clear()
        return ret


    def __str__(self) -> str:
        v = ""
        n = ""
        if len(self.verb_seq) != 0:
            v = "v" + ''.join(str(v) for v in self.verb_seq)
        if len(self.noun_seq) != 0:
            n = "n" + ''.join(str(n) for n in self.noun_seq)
        return v + n
    
    def __status(self) -> None:
        print("Status-------------")
        print("verb seq: " + ''.join(str(v) for v in self.verb_seq))
        print("noun seq: " + ''.join(str(n) for n in self.noun_seq))
        print("last action: " + self.last_action if self.last_action != None else "None")
        print("-------------------")