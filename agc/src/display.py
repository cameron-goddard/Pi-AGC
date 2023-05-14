import pygame
from pygame.locals import *
import math
import sys

class Display:
    """
    Handles updates to the right-hand side DSKY display.
    """

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()

        pygame.mouse.set_visible(0)
        
        # Constants
        self.screen_size = (240 * 2, 400 * 2)
        self.rect_height = self.screen_size[1]/5
        self.text_height = math.ceil((0.9)*self.rect_height)
        self.label_height = int(self.rect_height - self.text_height)
        self.font_dig = pygame.font.SysFont('Digital-7', self.text_height)
        self.font_cor = pygame.font.SysFont('Gill Sans MT', self.label_height*3)
        
        # Initialize screen sections and values
        if "RPi.GPIO" in sys.modules:
            self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.rowList = []
        self.boxList = []
        self.labelList = []
        self.rect_init()
        self.text_init()
        
        self.screen.fill((0,0,0))
        self.blit_all()
        
        pygame.display.flip()
        
    def rect_init(self) -> None:
        # three bottom rows, with r0 being the most bottom row
        r0 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*1), self.screen_size[0], self.rect_height)
        r1 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*2), self.screen_size[0], self.rect_height)
        r2 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*3), self.screen_size[0], self.rect_height)
        
        self.rowList = [[r0], [r1], [r2]]
        
        # verb, noun, prog, and comp rects
        prog = pygame.Rect((self.screen_size[0]*(2/3)), self.screen_size[1]-(self.rect_height*5)+self.rect_height*(0.2), (self.screen_size[0]*(1/3)), self.rect_height*(0.8))
        verb = pygame.Rect(0, self.screen_size[1]-(self.rect_height*4)+self.rect_height*(0.2), (self.screen_size[0]*(1/3)), self.rect_height*(0.8))
        noun = pygame.Rect((self.screen_size[0]*(2/3)), self.screen_size[1]-(self.rect_height*4)+self.rect_height*(0.2), (self.screen_size[0]*(1/3)), self.rect_height*(0.8))
        
        self.boxList = [[prog], [verb], [noun]]

        # rects that never change
        comp_label = pygame.Rect(0, int(self.screen_size[1]-(self.rect_height*4.6)), (self.screen_size[0]*(1/3)), self.rect_height*(1/2))
        prog_label = pygame.Rect((self.screen_size[0]*(2/3)), self.screen_size[1]-(self.rect_height*5), (self.screen_size[0]*(1/3)), self.rect_height*(0.2))
        verb_label = pygame.Rect(0, self.screen_size[1]-(self.rect_height*4), (self.screen_size[0]*(1/3)), self.rect_height*(0.2))
        noun_label = pygame.Rect((self.screen_size[0]*(2/3)), self.screen_size[1]-(self.rect_height*4), (self.screen_size[0]*(1/3)), self.rect_height*(0.2))
        
        self.labelList = [[comp_label], [prog_label], [verb_label], [noun_label]]
    
    
    def text_init(self) -> None:
        # row values
        r0_text = self.font_dig.render('000', False, (0, 255, 1))
        r1_text = self.font_dig.render('00000', False, (0, 255, 1))
        r2_text = self.font_dig.render('00000', False, (0, 255, 1))
        
        row_text = [r0_text, r1_text, r2_text]
        for i in range(len(self.rowList)):
            self.rowList[i].append(row_text[i])
            self.screen.blit(self.rowList[i][1], self.rowList[i][0])
        
        # prog, verb, and noun values
        prog_text = self.font_dig.render('', False, (0, 255, 1))
        verb_text = self.font_dig.render('00', False, (0, 255, 1))
        noun_text = self.font_dig.render('00', False, (0, 255, 1))
        
        box_text = [prog_text, verb_text, noun_text]
        for i in range(len(self.boxList)):
            self.boxList[i].append(box_text[i])
            self.screen.blit(self.boxList[i][1], self.boxList[i][0])
        
        # text that never changes
        comp_label_text = self.font_cor.render('COMP ACTY', False, (73, 73, 73))
        prog_label_text = self.font_cor.render('PROG', False, (0, 0, 0))
        verb_label_text = self.font_cor.render('VERB', False, (0, 0, 0))
        noun_label_text = self.font_cor.render('NOUN', False, (0, 0, 0))
        
        label_text = [comp_label_text, prog_label_text, verb_label_text, noun_label_text]
        for i in range(len(self.labelList)):
            self.labelList[i].append(label_text[i])
            self.screen.blit(self.labelList[i][1], self.labelList[i][0])
    
    def blit_all(self):
        for item in self.rowList:
            pygame.draw.rect(self.screen, (0,0,0), item[0])
            self.screen.blit(item[1], item[0])
        for item in self.boxList:
            pygame.draw.rect(self.screen, (0,0,0), item[0])
            self.screen.blit(item[1], item[0])
        pygame.draw.rect(self.screen, (0,0,0), self.labelList[0][0])
        self.screen.blit(self.labelList[0][1], self.labelList[0][0])
        for i in range(len(self.labelList)):
            if i != 0:
                pygame.draw.rect(self.screen, (0, 255, 1), self.labelList[i][0])
                self.screen.blit(self.labelList[i][1], self.labelList[i][0])
    
    def update_row(self, row: int, val: str) -> None:
        self.rowList[row][1] = self.font_dig.render(val, False, (0, 255, 1))
        self.screen.blit(self.rowList[row][1], self.rowList[row][0])
        self.blit_all()
        pygame.display.flip()
        

    def update_verb(self, val: str) -> None:
        self.boxList[1][1] = self.font_dig.render(val, False, (0, 255, 1))
        self.screen.blit(self.boxList[1][1], self.boxList[1][0])
        self.blit_all()
        pygame.display.flip()

    def update_noun(self, val: str) -> None:
        self.boxList[2][1] = self.font_dig.render(val, False, (0, 255, 1))
        self.screen.blit(self.boxList[2][1], self.boxList[2][0])
        self.blit_all()
        pygame.display.flip()

    def update_prog(self, val: str) -> None:
        self.boxList[0][1] = self.font_dig.render(val, False, (0, 255, 1))
        self.screen.blit(self.boxList[0][1], self.boxList[0][0])

    def clear_all(self, excluding: list[str] = []) -> None:
        if "noun" not in excluding:
            self.update_noun("")
        if "verb" not in excluding:
            self.update_verb("")
        if "0" not in excluding:
            self.update_row(0, "")
        if "1" not in excluding:
            self.update_row(1, "")
        if "2" not in excluding:
            self.update_row(2, "")
        if "prog" not in excluding:
            self.update_prog("")