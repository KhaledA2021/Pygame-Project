import pygame


class timer:

    def __init__(self):
        self.remaining_time = None

    def set_new_time(self, input):
        new_input = input*60
        self.remaining_time = new_input

    def count_down(self):
        if self.remaining_time is None:
            return False
        elif self.remaining_time > 0:
            self.remaining_time -= 1
        elif self.remaining_time <= 0:
            return True




