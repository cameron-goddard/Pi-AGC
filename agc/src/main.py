from dsky import DSKY
import pygame


if __name__ == "__main__":
    pygame.init()

    progs = []
    
    dsky = DSKY(progs)
    dsky.start()