import logging

class Parser:

    def __init__(self):
        logging.debug("Creating parser")
        self.verb = False
        self.noun = False
        self.seq = []

    def parse(self, key):
        logging.debug(key)
        


    def clear(self):
        self.verb = False
        self.noun = False
        self.seq.clear()
