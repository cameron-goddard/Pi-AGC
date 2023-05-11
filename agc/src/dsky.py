#import Rpi.GPIO as GPIO
import time
import pygame

from cmd_parser import Parser
from display import Display
from indicators import Indicators
from typing import Callable

class DSKY:
    """
    Manages all components of the DSKY interface and input processing.
    """

    def __init__(self) -> None:
        self.display = Display()
        self.indicators = Indicators()
        self.parser = Parser(self.display, self.indicators)
        self.progs = None

        self._boot_time = round(time.time(), 2)


        self.is_prog = False

    def init_progs(self, progs: list[Callable]) -> None:
        self.progs = progs

    def foo(self):
        print("in foo")

    def start(self) -> None:
        while True:
            # try:
            ret = None
            events = pygame.event.get()
            for event in events:

                # Handle key events (debugging)
                if event.type == pygame.KEYDOWN:
                    ret = self.parser.enter(pygame.key.name(event.key))
                
            self.display.blit_all()
            pygame.display.flip()
                        
                        
                        
            # except Exception as e:
            #     print(e)
            #     break

    def load_prog(self, id: int) -> int:
        """
        Loads a program to execute: V37E[id]E

        Args:
            id (int): The id of the program to load

        Returns:
            int: 0 if loading was successful, 1 if not
        """
        self.display.update_prog(id)
        prog = self.progs[id]
        prog(self)
        

    def _curr_time(self) -> float:
        """
        Gets the time since startup or last update

        Returns:
            float: The time, rounded to the nearest hundredth of a second
        """
        return round(time.time(), 2) - self._boot_time

    # Defined below are default computer-specific behaviors (programs)

    def lamp_test(self) -> None:
        """
        Basic DSKY lamp test: V35E
        """
        self.display.update_row(0, 88888)
        self.display.update_row(1, 88888)
        self.display.update_row(2, 88888)

        # TODO: flash verb, noun, key-rel, opr-err. Think about input interrupt

    def query_curr_time(self) -> None:
        """
        Queries the current time since startup or last update: V16N36E, V16N65E
        """
        pass

    def update_curr_time(self) -> None:
        """
        Updates the current time: V25N36E
        """
        pass

    def clear_screen(self) -> None:
        """
        Clears all content from the DSKY display and indicators: V36E
        """
        self.display.clear_all()
        self.indicators.clear_all()

    def show_vectors(self) -> None:
        """
        Shows velocity, altitude rate, altitude in R1, R2, R3 respectively: V06N62
        """
        pass

    def show_vectors_const(self) -> None:
        """
        Continuously shows velocity, altitude rate, altitude in R1, R2, R3 respectively: V16N62
        """
        pass