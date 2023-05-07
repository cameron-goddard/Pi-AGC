#import Rpi.GPIO as GPIO
import time
import pygame

from cmd_parser import Parser
from display import Display
from indicators import Indicators


class DSKY:

    def __init__(self) -> None:
        self.display = Display()
        self.indicators = Indicators()
        self.parser = Parser(self.display, self.indicators)

    def start(self) -> None:
        while True:
            # try:
                ret = None
                events = pygame.event.get()
                for event in events:

                    # Handle key events (debugging)
                    if event.type == pygame.KEYDOWN:
                        ret = self.parser.enter(pygame.key.name(event.key))
                        
                        
                        
            # except Exception as e:
            #     print(e)
            #     break

    def load(self) -> bool:
        pass

    # Defined below are default computer-specific behaviors (programs)

    def lamp_test(self) -> None:
        self.display.update_row(0, 88888)
        self.display.update_row(1, 88888)
        self.display.update_row(2, 88888)

        # TODO: flash verb, noun, key-rel, opr-err. Think about input interrupt