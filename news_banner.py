import curses
import time

class News:

    def __init__(self, message, width, speed):
        self.message = message
        self.width = width
        self.speed = speed
        self.padded_message = message + " " * width + message
        self.cycle_len = len(message) + width
        self.offset = 0
        
    def visible_text(self):
        return self.padded_message[self.offset:self.offset + self.width]

    def scroll(self):
        self.offset = (self.offset - 1) % (len(self.message) - 1)

    