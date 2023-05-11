from typing import Callable, Any
import dsky

class Program:

    def __init__(self, name: str, id: int, prog: Callable, dsky: dsky.DSKY) -> None:
        self.prog = prog
        self.dsky = dsky
        pass

    def exec(self) -> Any:
        self.prog(self.dsky)