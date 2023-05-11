from dsky import DSKY
import pygame

def test_prog(dsky: DSKY) -> None:
    print("hello")
    dsky.foo()
    print("after clear screen")

def idle(dsky: DSKY) -> None:
    while (True):
        continue


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    dsky = DSKY()
    progs = [test_prog]
    dsky.init_progs(progs)

    dsky.start()