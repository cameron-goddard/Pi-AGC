from display import Display
from indicators import Indicators

class Parser:
    """
    Reads in sequences of user input and returns a valid command or error.
    Updates the display and indicator lights as appropriate.
    """

    def __init__(self, display: Display, indicators: Indicators) -> None:
        self.display = display
        self.indicators = indicators

        self.verb_seq = []
        self.noun_seq = []

        self.last_action = None

    def enter(self, key: str) -> int:
        """
        Handles an input key from the DSKY and returns the status after keystroke

        Args:
            key (str): A valid keystroke

        Returns:
            int: A valid id for a program, -1 for an error, or -2 for incomplete
        """
        
        if key == "v":
            self.last_action = "verb"

            if len(self.noun_seq) != 0:
                self.display.clear_all(excluding="noun")
            else:
                self.display.clear_all()
            
        elif key == "n":
            self.last_action = "noun"
            
            if len(self.verb_seq) != 0:
                self.display.clear_all(excluding="verb")
            else:
                self.display.clear_all()

        elif key == "program":
            pass
        elif key == "key-release":
            pass
        elif key == "reset":
            pass
        elif key == "return":
            if self.last_action == None:
                # TODO: flash opr err indicator
                pass

            self.last_action = None
            print(self)
            self.clear()
            return self._parse()
        else:
            if len(self.noun_seq) != 0 and len(self.verb_seq) == 0:
                # TODO: flash opr err indicator
                pass

            if self.last_action == "verb":
                if len(self.verb_seq) < 2:
                    self.verb_seq.append(key)
            elif self.last_action == "noun":
                if len(self.noun_seq) < 2:
                    self.noun_seq.append(key)
            else:
                self.display.clear_all()
            
                
    def clear(self) -> None:
        self.verb_seq = []
        self.verb = False

        self.noun_seq = []
        self.noun = False

    def _parse(self):
        pass

    def __str__(self) -> str:
        v = ""
        n = ""
        if len(self.verb_seq) != 0:
            v = "v" + ''.join(str(v) for v in self.verb_seq)
        if len(self.noun_seq) != 0:
            n = "n" + ''.join(str(n) for n in self.noun_seq)
        return v + n