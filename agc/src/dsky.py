#import RPi.GPIO as GPIO
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
        self.progs = []

        self._boot_time = round(time.time(), 2)


        self.current_prog = -1

    def init_progs(self, progs: list[Callable]) -> None:
        self.progs = progs

    def foo(self):
        self.display.update_row(0, "42")
        print("in foo")

    def start(self) -> None:
        while True:
            try:
                ret = None
                events = pygame.event.get()
            
                for event in events:

                

                    # Handle key events (debugging)
                    if event.type == pygame.KEYDOWN:
                        ret = self.parser.enter(pygame.key.name(event.key))

                        if ret == -1:
                            print("error")
                            self.display.clear_all(excluding=["prog"])
                        elif ret == -2:
                            print("more to come")
                            pass
                        elif ret >= 0:
                            print("prog")
                            print(type(ret))
                            print(ret)
                            self.load_prog(ret)
                        else:
                            print("returned " + str(ret))
                            if ret == -5:
                                self.lamp_test()
                            if ret == -6:
                                self.query_curr_time()
                            if ret == -7:
                                self.update_curr_time()

                
                self.display.blit_all()
                pygame.display.flip()
                        
            except KeyboardInterrupt:
                GPIO.cleanup()  
                        
            except Exception as e:
                print(e)
                break

    def load_prog(self, id: int) -> int:
        """
        Loads a program to execute: V37E[id]E

        Args:
            id (int): The id of the program to load

        Returns:
            int: 0 if loading was successful, 1 if not
        """
        if id >= len(self.progs):
            self.display.clear_all()
            # TODO: flash error indicator
            return 1
        
        self.current_prog = id
        self.display.update_prog(double_str(id))
        self.display.clear_all(excluding=["prog"])
        # TODO: flash comp acty
        
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
        self.display.update_prog("88")
        self.display.update_verb("88")
        self.display.update_noun("88")
        self.display.update_row(0, "88888")
        self.display.update_row(1, "88888")
        self.display.update_row(2, "88888")

        # TODO: flash verb, noun, key-rel, opr-err. Think about input interrupt

    def query_curr_time(self) -> None:
        """
        Queries the current time since startup or last update: V16N36E, V16N65E
        """
        local = time.localtime(self._curr_time())

        self.display.update_row(0, str(local.tm_hour))
        self.display.update_row(1, str(local.tm_min))
        self.display.update_row(2, str(int((self._curr_time() % 1) * 100)))


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



def double_str(num: int) -> str:
    if num < 10:
        return "0" + str(num)
    return str(num)