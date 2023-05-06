#import Rpi.GPIO as GPIO
import time
import pygame

from cmd_parser import Parser
from display import Display
from indicators import Indicators


class DSKY:

    def __init__(self):
        self.display = Display()
        self.indicators = Indicators()
        self.parser = Parser(self.display, self.indicators)

    def run(self):
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
