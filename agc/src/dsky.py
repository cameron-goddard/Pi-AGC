try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
import time
import pygame
import csv
import os

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
        self.interrupted = False

    def init_progs(self, progs: list[Callable]) -> None:
        self.progs = progs

    def verb_keyed(self, channel):
        self.parser.enter("v")
        self.interrupted = True

    def noun_keyed(self, channel):
        self.parser.enter("n")
        self.interrupted = True

    def prog_keyed(self, channel):
        self.current_prog = -1

    def start(self) -> None:
        while True:
            # ret = None
            # key = "99"

            
            
                
            # if self.current_prog == -1:
            #     if key != "99":
            #         ret = self.parser.enter(key)

            #     if ret == -1:
            #         self.display.clear_all(excluding=["prog"])
            #     elif ret == -2:
            #         pass
            #     elif ret >= 0:
            #         self.load_prog(ret)
            #     else:
            #         if ret == -5:
            #             self.lamp_test()
            #         if ret == -6:
            #             self.query_curr_time()
            #         if ret == -7:
            #             self.update_curr_time()
            #         if ret == -8:
            #             self.show_vectors()
            #         if ret == -9:
            #             self.show_alarm_codes()
            # else:
            #     ret = self.progs[self.current_prog](self, key)

            #     if ret == 0:
            #         self.current_prog = -1

            # self.display.blit_all()
            # pygame.display.flip()


                events = pygame.event.get()
                for event in events:
                    # Handle key events (debugging)
                    if event.type == pygame.KEYDOWN:
                        if self.current_prog == -1:
                            ret = self.parser.enter(pygame.key.name(event.key))

                            if ret == -1:
                                self.display.clear_all(excluding=["prog"])
                                self.indicators.indicator_on("OPR ERR")
                                self.indicators.indicator_off("PROG")
                                # Flash error indicator
                            elif ret == -2:
                                self.indicators.indicator_off("OPR ERR")
                                
                            elif ret >= 0:
                                self.indicators.indicator_off("OPR ERR")
                                self.indicators.indicator_on("PROG")
                                self.load_prog(ret)
                            else:
                                self.indicators.indicator_off("OPR ERR")
                                self.indicators.indicator_off("PROG")
                                if ret == -5:
                                    self.lamp_test()
                                if ret == -6:
                                    self.query_curr_time()
                                if ret == -7:
                                    self.update_curr_time()
                                if ret == -8:
                                    self.show_vectors()
                                if ret == -9:
                                    self.show_alarm_codes()
                                if ret == -10:
                                    self.quit_prog()
                        else:
                            ret = self.progs[self.current_prog](self, pygame.key.name(event.key))

                            if ret == 0:
                                self.current_prog = -1
                                
                self.display.blit_all()
                pygame.display.flip()

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
        prog(self, None)
        

    def _curr_time(self) -> float:
        """
        Gets the time since startup or last update

        Returns:
            float: The time, rounded to the nearest hundredth of a second
        """
        print("curr time: ", round(time.time(), 2) - self._boot_time)
        return round(time.time(), 2) - self._boot_time

    # Defined below are default computer-specific behaviors (programs)

    def lamp_test(self) -> None:
        """
        Basic DSKY lamp test: V35E
        """
        self.interrupted = False

        self.display.update_row(0, "88888")
        self.display.update_row(1, "88888")
        self.display.update_row(2, "88888")
        self.display.update_prog("88")

        self.indicators.indicator_on("TEMP")
        self.indicators.indicator_on("OPR ERR")
        self.indicators.indicator_on("PROG")

        elapsed = 0.5
        while (not self.interrupted and elapsed < 4):
            self.display.update_verb("88")
            self.display.update_noun("88")
            time.sleep(0.5)
            elapsed += 0.5
           
            self.display.update_verb("")
            self.display.update_noun("")
            time.sleep(0.5)
            elapsed += 0.5

        self.indicators.indicator_off("TEMP")
        self.indicators.indicator_off("OPR ERR")
        self.indicators.indicator_off("PROG")
        

    def query_curr_time(self) -> None:
        """
        Queries the current time since startup or last update: V16N36E, V16N65E
        """
        self.interrupted = False
        rounded = round(self._curr_time(), 2)

        while (not self.interrupted):
            rounded = round(self._curr_time(), 2)
            secs = str(int(rounded / 3600))
            mins = str(int(rounded / 60))
            hours = str(int(rounded * 100))

            self.display.update_row(2, "0" * (5 - len(secs)) + secs)
            self.display.update_row(1, "0" * (5 - len(mins)) + mins)
            self.display.update_row(0, "0" * (5 - len(hours)) + hours)
            time.sleep(1)

    def update_curr_time(self) -> None:
        """
        Updates the current time: V25N36E
        """
        
    def show_alarm_codes(self) -> None:
        """
        Shows recent alarm codes: V05N09E
        """
        self.display.update_row(2, "01105")
        self.display.update_row(1, "01106")
        self.display.update_row(0, "00000")

    def clear_screen(self) -> None:
        """
        Clears all content from the DSKY display and indicators: V36E
        """
        self.display.clear_all()
        self.indicators.clear_all()

    def reset_screen(self) -> None:
        self.display.update_noun("00")
        self.display.update_verb("00")
        self.display.update_prog("  ")
        self.display.update_row(2, "00000")
        self.display.update_row(1, "00000")
        self.display.update_row(0, "000")

    def quit_prog(self) -> None:
        os.exit()

    def show_vectors(self) -> None:
        """
        Shows x, y, z velocity in R1, R2, R3 respectively: V06N62
        """
        self.interrupted = False
        vecs = []
        with open('apollo11_launch.csv') as csvfile:
            reader = csv.reader(csvfile)
            first = True
            for row in reader:
                if first:
                    first = False
                    continue
                vecs.append([round(float(x), 2) for x in row])
        
        i = 0
        while (not self.interrupted):
            self.display.update_row(2, ("   " + str(int(vecs[i][0] * 100)) if vecs[i][0] >= 0 else "-  " + str(abs(int(vecs[i][0] * 100)))))
            self.display.update_row(1, ("   " + str(int(vecs[i][1] * 100)) if vecs[i][1] >= 0 else "-  " + str(abs(int(vecs[i][1] * 100)))))
            self.display.update_row(0, ("   " + str(int(vecs[i][2] * 100)) if vecs[i][2] >= 0 else "-  " + str(abs(int(vecs[i][2] * 100)))))
            time.sleep(3)
            i = (i + 1) % len(vecs)
        
def double_str(num: int) -> str:
    if num < 10:
        return "0" + str(num)
    return str(num)