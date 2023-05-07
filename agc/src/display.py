import pygame
import math

class Display:
    """
    Handles updates to the right-hand side DSKY display.
    """

    def __init__(self) -> None:
        #pygame.init()
        
        # Constants
        self.screen_size = (240, 400)
        self.rect_height = self.screen_size[1]/5
        self.text_height = math.ceil((2/3)*self.rect_height)
        self.bar_height = self.rect_height - self.text_height
        
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.r0 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*1), self.screen_size[0], self.rect_height)
        self.r1 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*2), self.screen_size[0], self.rect_height)
        self.r2 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*3), self.screen_size[0], self.rect_height)
        self.r3 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*4), self.screen_size[0], self.rect_height)
        self.r4 = pygame.Rect(0, self.screen_size[1]-(self.rect_height*5), self.screen_size[0], self.rect_height)
        
        # code_run = True
        
        # while code_run:
        #     for event in pygame.event.get():
        #         print("in this other loop")
        #         if event.type == pygame.QUIT:
        #             code_run = False
            
        #     self.screen.fill("black")
        #     pygame.draw.rect(self.screen, "black", self.r0)
        #     pygame.draw.rect(self.screen, "black", self.r1)
        #     pygame.draw.rect(self.screen, "black", self.r2)
        #     pygame.draw.rect(self.screen, "black", self.r3)
        #     pygame.draw.rect(self.screen, "black", self.r4)
            
            
        #     pygame.display.flip()
        
        # pygame.quit()
        

    def update_row(self, row: int, val: int) -> None:
        pass

    def update_verb(self, val: int) -> None:
        pass

    def update_noun(self, val: int) -> None:
        pass

    def update_prog(self, val: int) -> None:
        pass

    def clear_all(self, excluding: str = None) -> None:
        pass
    
#d = Display()